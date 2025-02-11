from typing import Callable
import RPi.GPIO as GPIO, time
from dataclasses import dataclass, field
from .PWM import PWM

class Drive():
    L_F: int
    L_R: int
    R_F: int
    R_R: int
    ENA: PWM
    ENB: PWM
    
    speed = 50
    
    debug: bool = False
    
    def __init__(self, l_in1, l_in2, l_pwm, r_in1, r_in2, r_pwm, debug=False) -> None:
        self.L_F = l_in1
        self.L_R = l_in2
        self.R_F = r_in1
        self.R_R = r_in2
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.L_F, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.L_R, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.R_F, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.R_R, GPIO.OUT, initial=GPIO.LOW)
        
        self.ENA = PWM(l_pwm, 2000, 0)
        self.ENB = PWM(r_pwm, 2000, 0)
        self.ENA.start(0)
        self.ENB.start(0)
        
        self.debug = debug
        
    def __del__(self):
        self.stop()
        GPIO.cleanup([self.L_F, self.L_R, self.R_F, self.R_R])
        
    def set_speed(self, speed):
        self.speed = int(speed)
        self.ENA.set_duty_cycle(self.speed)
        self.ENB.set_duty_cycle(self.speed)
        print(f"Set speed to {self.speed}")
        
    def delta_speed(self, delta):
        self.speed += delta
        if self.speed < 0: self.speed = 0
        if self.speed > 100: self.speed = 100
        self.ENA.set_duty_cycle(self.speed)
        self.ENB.set_duty_cycle(self.speed)
        print(f"Set speed to {self.speed}")
        
    #region Basic motor movement functions
    def forward(self, speed=None):
        """ Move forward for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.0.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.LM_forward(speed)
        self.RM_forward(speed)

    def reverse(self, speed=None):
        """ Move backward for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.0.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.LM_reverse(speed)
        self.RM_reverse(speed)

    def turn_left(self, speed=None):
        """ Turn left for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.0.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.RM_forward(speed)

    def turn_right(self, speed=None):
        """ Turn right for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.0.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.LM_forward(speed)

    def rotate_left(self, speed=None):
        """ Rotate left for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.LM_reverse(speed)
        self.RM_forward(speed)

    def rotate_right(self, speed=None):
        """ Rotate right for a specified duration and speed

        Args:
            duration (float, optional): _float_ Time in seconds. Defaults to 1.
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        self.LM_forward(speed)
        self.RM_reverse(speed)

    def stop(self):
        """ Stops all track motors """
        print("Stopping")
        GPIO.output(self.L_F, GPIO.LOW)
        GPIO.output(self.L_R, GPIO.LOW)
        GPIO.output(self.R_F, GPIO.LOW)
        GPIO.output(self.R_R, GPIO.LOW)
    #endregion
    
    #region Advanced motor movement functions
    def LM_forward(self, speed=None):
        """ Move left motor forward at a specified speed

        Args:
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        if speed is None: speed = self.speed
        else: self.speed = int(speed)
        print(f"Moving Left Motor Forward: {speed}")
        self.ENA.set_duty_cycle(speed)
        GPIO.output(self.L_F, GPIO.HIGH)
        GPIO.output(self.L_R, GPIO.LOW)
        
    def LM_reverse(self, speed=None):
        """ Move left motor backward at a specified speed

        Args:
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        if speed is None: speed = self.speed
        else: self.speed = int(speed)
        print(f"Moving Left Motor Backward: {speed}")
        self.ENA.set_duty_cycle(speed)
        GPIO.output(self.L_F, GPIO.LOW)
        GPIO.output(self.L_R, GPIO.HIGH)
        
    def RM_forward(self, speed=None):
        """ Move right motor forward at a specified speed

        Args:
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        if speed is None: speed = self.speed
        else: self.speed = int(speed)
        print(f"Moving Right Motor Forward: {speed}")
        self.ENB.set_duty_cycle(speed)
        GPIO.output(self.R_F, GPIO.HIGH)
        GPIO.output(self.R_R, GPIO.LOW)
        
    def RM_reverse(self, speed=None):
        """ Move right motor backward at a specified speed

        Args:
            speed (int, optional): _int_ Motor speed. Defaults to 50.
        """
        if speed is None: speed = self.speed
        else: self.speed = int(speed)
        print(f"Moving Right Motor Backward: {speed}")
        self.ENB.set_duty_cycle(speed)
        GPIO.output(self.R_F, GPIO.LOW)
        GPIO.output(self.R_R, GPIO.HIGH)
    #endregion