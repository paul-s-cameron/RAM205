'''warning3.py
Blinks the warning LED and sounds the buzzer using PWM
'''

import RPi.GPIO as GPIO
import time

WARN_LED_PIN = 22
BUZZER_PIN = 24

WARN_LED_ON = GPIO.HIGH
BUZZER_ON = GPIO.LOW

# Configure GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Pin setup
GPIO.setup(WARN_LED_PIN, GPIO.OUT, initial= not WARN_LED_ON)
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial= not BUZZER_ON)

# PWM setup
pwm_Warner = GPIO.PWM(WARN_LED_PIN, 0.5)
pwm_Buzzer = GPIO.PWM(BUZZER_PIN, 0.5)

pwm_Warner.start(50.0)
time.sleep(0.5)
pwm_Buzzer.start(80.0)

time.sleep(10.0)

GPIO.cleanup()