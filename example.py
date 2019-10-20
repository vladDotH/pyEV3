from ev3 import Ev3
import time

bot = Ev3("COM4")

bot.set_speed(Ev3.Motors.A, 40)
bot.start(Ev3.Motors.A)

time.sleep(1)

bot.set_speed(Ev3.Motors.A, -40)
bot.start(Ev3.Motors.A)

time.sleep(1)

bot.set_speed(Ev3.Motors.A, 0)
bot.stop(Ev3.Motors.A, Ev3.Stop.FLOAT)

time.sleep(1)
