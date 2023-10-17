# type: ignore

import board
import time
import adafruit_mpu6050
import busio


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(f'X = {mpu.acceleration[0]}\n Y = { mpu.acceleration[1]}\n Z = { mpu.acceleration[2]}')
    time.sleep(.1)
