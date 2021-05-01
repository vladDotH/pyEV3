Библиотека для управления блоком 'LEGO™ EV3' посредством Bluetooth соединения. 

#### Установка

`pip install ev3-python`
или
`pip3 install ev3-python`

#### Использование

```python
from ev3 import Ev3
import serial
import time

# Указываем последовательный порт в конструкторе 'COM...'
bot = Ev3("COM5")
# Для linux '/dev/ttyS...'

# Установка скорости мотора [-127..127]
bot.set_speed(Ev3.Motors.A, 127)

# Запуск мотора
bot.start(Ev3.Motors.A)

#Время вращения мотора
time.sleep(2)

# Остановка мотора  
bot.stop(Ev3.Motors.A, Ev3.Stop.FLOAT)
# Второй аргумент `type` - тип остановки: BREAK - с фиксацией мотора, FLOAT - без

#Завершение работы с контроллером
bot.close()
```
