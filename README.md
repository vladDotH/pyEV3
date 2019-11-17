Библиотека для управления блоком 'LEGO™ EV3' посредтством Bluetooth соединения. 

#Установка

`pip install ev3-python`
или
`pip3 install ev3-python`

#Использование

```python
from ev3 import Ev3

# Указываем последовательный порт в конструкторе 'COM...'
bot = Ev3("COM...")
# Для linux '/dev/ttyS...'

# Задаём скорость для мотора N[-100..100]
bot.set_speed(Ev3.Motors.A, N)

# Запуск мотора
bot.start(Ev3.Motors.A)

# Остановка мотора  
bot.stop(Ev3.Motors.A, Ev3.Stop.FLOAT)
# Второй аргумент `type` - тип остановки: BREAK - с фиксацией мотора, FLOAT - без
```
