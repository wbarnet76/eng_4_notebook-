# type: ignore

import board
import time
import digitalio
import pwmio
from adafruit_motor import servo


pwm_servo = pwmio.PWMOut(board.GP13, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

green = digitalio.DigitalInOut(board.GP15)
green.direction = digitalio.Direction.OUTPUT


red = digitalio.DigitalInOut(board.GP16)
red.direction = digitalio.Direction.OUTPUT


button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


import time 

servo1.angle = 0

while True: 
    if button.value == False:    
      for x in range(11):
        print(10-x)
        red.value = True
        time.sleep(1)
        red.value = False
        time.sleep(1)



      while True:
        green.value = True
        print("liftoff")
        
        servo1.angle = 180
        
    