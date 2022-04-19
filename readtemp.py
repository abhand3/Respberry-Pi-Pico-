from time import sleep
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from machine import Pin

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

tempsensor = ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    currentvoltage = tempsensor.read_u16()* conversion_factor
    tempLong = 27 - ((currentvoltage - 0.706)/ 0.001721)
    temp = "{:.2f}".format(tempLong)
    print(str(currentvoltage) + ":" + str(temp))
    lcd.move_to(0,0)
    lcd.putstr("Temp:" + temp)
    lcd.move_to(0,1)
    lcd.putstr("Volt: {:.3f}".format(currentvoltage))
    sleep(2)
