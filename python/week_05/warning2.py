'''warning2.py
Blinks the warning LED and sounds the buzzer
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

for i in range(0, 20):
    GPIO.output(WARN_LED_PIN, WARN_LED_ON)
    GPIO.output(BUZZER_PIN, BUZZER_ON)
    time.sleep(1)
    GPIO.output(WARN_LED_PIN, not WARN_LED_ON)
    GPIO.output(BUZZER_PIN, not BUZZER_ON)
    time.sleep(1)
    
GPIO.cleanup()