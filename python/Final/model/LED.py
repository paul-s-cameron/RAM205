import RPi.GPIO as GPIO
from .PWM import PWM

class LED:
    color: list = [255, 255, 255]
    brightness: int = 100
    frequency: float = 1000
    enabled: bool = False
    
    R: PWM
    G: PWM
    B: PWM
    
    debug: bool = False
    
    def __init__(self, red_pin=22, green_pin=27, blue_pin=24, debug=False) -> None:
        self.R = PWM(red_pin, 1000, 0)
        self.R.name = "Red LED"
        self.G = PWM(green_pin, 1000, 0)
        self.G.name = "Green LED"
        self.B = PWM(blue_pin, 1000, 0)
        self.B.name = "Blue LED"
        self.R.start()
        self.G.start()
        self.B.start()
        
        self.debug = debug
        
    def enable(self, leds: list):
        if not isinstance(leds, list): leds = [leds]
        for led in leds:
            if not isinstance(led, PWM):
                print(f"Invalid LED: {led}")
                continue
            led.start()
            led.set_duty_cycle(100)

    def on(self):
        self.R.start()
        self.G.start()
        self.B.start()
        self.enabled = True

    def off(self):
        self.R.stop()
        self.G.stop()
        self.B.stop()
        self.enabled = False
        
    def set_color(self, red: int = None, green: int = None, blue: int = None):
        """ Set the color of the LED

        Args:
            red (int): _int_ 0-255
            green (int): _int_ 0-255
            blue (int): _int_ 0-255
        """
        if self.debug: print(f"Setting LED color to {red}, {green}, {blue}")
        if red is not None:
            self.color[0] = red
            self.R.set_frequency(self.frequency)
            self.R.set_duty_cycle(self.brightness * (red / 255))
        if green is not None:
            self.color[1] = green
            self.G.set_frequency(self.frequency)
            self.G.set_duty_cycle(self.brightness * (green / 255))
        if blue is not None:
            self.color[2] = blue
            self.B.set_frequency(self.frequency)
            self.B.set_duty_cycle(self.brightness * (blue / 255))
        
    def set_brightness(self, brightness: int):
        """ Set the brightness of the LED

        Args:
            brightness (int): _int_ 0-100
        """
        if self.debug: print(f"Setting LED brightness to {brightness}%")
        self.brightness = brightness
        self.set_color(*self.color)

    def blink(self, leds: list, duty_cycle: float, frequency: float):
        """ Blink the LEDs

        Args:
            leds (list): LEDs to blink
            duty_cycle (float): duty cycle (0-100)
            frequency (float): frequency (Hz)
        """
        if self.debug: print(f"Blinking {leds} with duty cycle {duty_cycle} and frequency {frequency}")
        if isinstance(leds, PWM): leds = [leds]
        for led in leds:
            if not isinstance(led, PWM):
                print(f"Invalid LED: {led}")
                continue
            led.set_duty_cycle(duty_cycle)
            led.set_frequency(frequency)
            led.start()