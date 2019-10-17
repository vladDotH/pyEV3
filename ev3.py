import serial
import time
from serial import Serial


class Ev3:
    class MsgType:
        class Mode:
            first = 0
            second = 0

        speed = Mode()
        start = Mode()
        stop = Mode()

        speed.first = 10
        speed.second = 165

        start.first = 8
        start.second = 166

        stop.first = 9
        stop.second = 163

    class Motors:
        A = 0b1
        B = 0b10
        C = 0b100
        D = 0b1000

    class Stop:
        FLOAT = 0
        BREAK = 1

    def __init__(self, portName: str) -> None:
        self.ev3 = Serial(portName, baudrate=9600,
                          stopbits=serial.STOPBITS_ONE,
                          parity=serial.PARITY_NONE,
                          bytesize=serial.EIGHTBITS)

        time.sleep(1)

    def setSpeed(self, motor, val):
        message = self.packMsg(self.MsgType.speed)

        if val < 0:
            val = 256 - abs( val )

        for i in range(0, 3):
            message.append(0)

        message[9] = motor
        message[10] = 129
        message[11] = val


        self.send(message)

    def start(self, motor):
        message = self.packMsg(self.MsgType.start)

        for i in range(0, 1):
            message.append(0)

        message[9] = motor

        self.send(message)

    def stop(self, motor, type):
        message = self.packMsg(self.MsgType.stop)

        for i in range(0, 2):
            message.append(0)

        message[9] = motor
        message[10] = type

        self.send(message)

    def send(self, message):
        self.ev3.write(bytes(message))

    def packMsg(self, mode):
        msg = []
        for i in range(0, 9):
            msg.append(0)

        msg[0] = mode.first
        msg[7] = mode.second
        msg[4] = 128

        return msg

    def close(self):
        self.ev3.close()

    def __del__(self):
        self.close()
