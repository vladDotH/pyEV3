Библиотека для управления блоком 'LEGO™ EV3' посредством Bluetooth соединения. 

### Установка

`pip install ev3-python`
или
`pip3 install ev3-python`

### Использование

#### Подключение
```python
from ev3 import Ev3

# Указываем последовательный порт в конструкторе 'COM...'
bot = Ev3("COM...")
# Для linux '/dev/ttyS...'

# После использования желательно закрыть порт
bot.close()
```

#### Использование моторов
```python
# Моторы: Ev3.Motors.[A, B, C, D]

# Установка скорости для мотора N[-128..127]
bot.set_speed(Ev3.Motors.A, N)

# Запуск мотора
bot.start(Ev3.Motors.A)

# Остановка мотора  
bot.stop(Ev3.Motors.A, Ev3.Stop.FLOAT)
# Второй аргумент `type` - тип остановки: BREAK - с фиксацией мотора, FLOAT - без
```
#### Использование сенсоров
```python
# Порты: Ev3.Ports.[P1, P2, P3, P4]

# Получение исходного значения
bot.getRaw(Ev3.Ports.P1)

# Кнопка : {True, False}
bot.button(Ev3.Ports.P1)

# Ультразвуковой дальномер (в миллиметрах) : [30, 2550]
bot.ultrasonic(Ev3.Ports.P1)

# Инфракрасный датчик : [0, 100] (минимум 0 - Чёрное, максимум 100 - Белое)
bot.color(Ev3.Ports.P1)

# Энкодеры: Ev3.Encoders.[A, B, C, D]
bot.encoder(Ev3.Encoders.A)
```