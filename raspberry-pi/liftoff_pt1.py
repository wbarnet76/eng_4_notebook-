# type: ignore

import board
import time
import digitalio
green = digitalio.DigitalInOut(board.GP15)
green.direction = digitalio.Direction.OUTPUT


red = digitalio.DigitalInOut(board.GP16)
red.direction = digitalio.Direction.OUTPUT
import time 

for x in range(11):
  if x<10:
    print(10-x)
    time.sleep(1)

  if 10-x:
    red.value = True
    time.sleep(1)
    red.value = False



while True:
  green.value = True
  print("liftoff")