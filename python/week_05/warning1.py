'''warning1.py
Blinks the warning LED
'''

import RPi.GPIO as GPIO
import time

HEADER_5 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(HEADER_5, GPIO.OUT)

for i in range(0, 20):
    GPIO.output(HEADER_5, True)
    time.sleep(1)
    GPIO.output(HEADER_5, False)
    time.sleep(1)