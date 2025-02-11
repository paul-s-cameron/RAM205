'''piRover_Warner module
Module that blinks the warning LED and sounds the buzzer using PWM
'''

import RPi.GPIO as GPIO
import time

WARN_LED_PIN = 22
BUZZER_PIN = 24

pwm_Warner = None
pwm_Buzzer = None

def warn_init():
    global pwm_Warner, pwm_Buzzer
    # Configure GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # Pin setup
    GPIO.setup(WARN_LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.HIGH)

    # PWM setup
    pwm_Warner = GPIO.PWM(WARN_LED_PIN, 0.5)
    pwm_Buzzer = GPIO.PWM(BUZZER_PIN, 0.5)

def warn_start():
    if not pwm_Warner or not pwm_Buzzer: # Python error handling 🤮
        print("The pwm's have not been initialized properly")
        return
    pwm_Warner.start(50.0)
    time.sleep(0.5)
    pwm_Buzzer.start(80.0)
    
def warn_stop():
    if not pwm_Warner or not pwm_Buzzer:
        print("The pwm's have not been initialized properly")
        return
    pwm_Warner.stop()
    pwm_Buzzer.stop()