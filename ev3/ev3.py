import threading
import serial
import time
from serial import Serial


class Ev3:
    class _MsgType:
        class Mode:
            def __init__(self, first, second):
                self.second = second
                self.first = first

        Speed = Mode(10, 165)
        Start = Mode(8, 166)
        Stop = Mode(9, 163)
        GetRaw = Mode(14, 153)

    class Motors:
        A = 0b0001
        B = 0b0010
        C = 0b0100
        D = 0b1000

    class Stop:
        FLOAT = 0
        BREAK = 1

    class Ports:
        P1 = 0b00
        P2 = 0b01
        P3 = 0b10
        P4 = 0b11

    class Encoders:
        A = 0b10000
        B = 0b10001
        C = 0b10010
        D = 0b10011

    class _Reply:
        Need = 0
        No_Need = 128

    _RAW_SIZE = 9
    _BUTTON_THRESHOLD = 0x400

    @staticmethod
    def clip(val, _min, _max):
        return min(_max, max(val, _min))

    def __init__(self, port_name):
        self._controller = Serial(port_name,
                                  baudrate=9600,
                                  stopbits=serial.STOPBITS_ONE,
                                  parity=serial.PARITY_NONE,
                                  bytesize=serial.EIGHTBITS,
                                  timeout=1)
        time.sleep(0.3)
        self._lock = threading.Lock()

    def set_speed(self, motor, val):
        message = self._pack_msg(self._MsgType.Speed)
        val = self.clip(val, -128, 127)
        if val < 0:
            val = 256 - abs(val)
        message.extend([0] * 3)
        message[9] = motor
        message[10] = 129
        message[11] = val
        self._send(message)

    def start(self, motor):
        message = self._pack_msg(self._MsgType.Start)
        message.extend([0] * 1)
        message[9] = motor
        self._send(message)

    def stop(self, motor, type):
        message = self._pack_msg(self._MsgType.Stop)
        message.extend([0] * 2)
        message[9] = motor
        message[10] = type
        self._send(message)

    def getRaw(self, port):
        message = self._pack_msg(self._MsgType.GetRaw, self._Reply.Need)
        message.extend([0] * 7)
        message[5] = 4
        message[8] = 11
        message[10] = port
        message[11] = 227
        self._send(message)
        raw = self._recv(self._RAW_SIZE)
        return int.from_bytes(raw[-4:], 'little')

    def button(self, port):
        return self.getRaw(port) >= self._BUTTON_THRESHOLD

    def ultrasonic(self, port):
        return self.getRaw(port)

    def color(self, port):
        return self.getRaw(port)

    def encoder(self, port):
        return self.getRaw(port)

    def _send(self, message):
        try:
            self._lock.acquire()
            self._controller.write(bytes(message))
        finally:
            self._lock.release()

    def _recv(self, size):
        try:
            self._lock.acquire()
            return self._controller.read(size)
        finally:
            self._lock.release()

    @staticmethod
    def _pack_msg(mode, reply=_Reply.No_Need):
        msg = [0] * 9
        msg[0] = mode.first
        msg[7] = mode.second
        msg[4] = reply
        return msg

    def close(self):
        self._controller.close()
        time.sleep(2)

    def __del__(self):
        self.close()
