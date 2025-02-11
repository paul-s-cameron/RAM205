import RPi.GPIO as GPIO, time
from .Servo import Servo

class Gimbal():
    horizontal: Servo
    vertical: Servo
    
    def __init__(self, horizontal_pin=11, vertical_pin=9, debug=False):
        self.horizontal = Servo(pin=horizontal_pin, debug=debug)
        self.horizontal.name = "Gimbal Horizontal"
        self.vertical = Servo(pin=vertical_pin, debug=debug)
        self.vertical.name = "Gimbal Vertical"
        
    def set_pos(self, horizontal=90, vertical=90):
        """ Set gimbal position

        Args:
            horizontal (int, optional): _int_ 0-180 Degrees. Defaults to 90.
            vertical (int, optional): _int_ 0-180 Degrees. Defaults to 90.
        """
        self.horizontal.set_pos(horizontal)
        self.vertical.set_pos(vertical)
        
    def delta_pos(self, delta_horizontal, delta_vertical):
        self.horizontal.delta_pos(delta_horizontal)
        self.vertical.delta_pos(delta_vertical)