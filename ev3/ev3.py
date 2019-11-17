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

        speed = Mode(10, 165)
        start = Mode(8, 166)
        stop = Mode(9, 163)

    class Motors:
        A = 0b1
        B = 0b10
        C = 0b100
        D = 0b1000

    class Stop:
        FLOAT = 0
        BREAK = 1

    def __init__(self, port_name):
        self._controller = Serial(port_name, baudrate=9600,
                                  stopbits=serial.STOPBITS_ONE,
                                  parity=serial.PARITY_NONE,
                                  bytesize=serial.EIGHTBITS)

        time.sleep(1)
        self._lock = threading.Lock()

    def set_speed(self, motor, val):
        message = self._pack_msg(self._MsgType.speed)

        if val < 0:
            val = 256 - abs(val)

        for i in range(0, 3):
            message.append(0)

        message[9] = motor
        message[10] = 129
        message[11] = val

        self._send(message)

    def start(self, motor):
        message = self._pack_msg(self._MsgType.start)

        for i in range(0, 1):
            message.append(0)

        message[9] = motor

        self._send(message)

    def stop(self, motor, type):
        message = self._pack_msg(self._MsgType.stop)

        for i in range(0, 2):
            message.append(0)

        message[9] = motor
        message[10] = type

        self._send(message)

    def _send(self, message):
        try:
            self._lock.acquire()
            self._controller.write(bytes(message))
        finally:
            self._lock.release()

    @staticmethod
    def _pack_msg(mode):
        msg = [0 for i in range(9)]
        msg[0] = mode.first
        msg[7] = mode.second
        msg[4] = 128

        return msg

    def close(self):
        self._controller.close()

    def __del__(self):
        self.close()
