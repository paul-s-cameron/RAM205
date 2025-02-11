'''warning4.py
Uses the piRover_Warner module
'''

import RPi.GPIO as GPIO
import time

from piRover_Warner import *

warn_init()

warn_start()

time.sleep(10.0)

warn_stop()

GPIO.cleanup()