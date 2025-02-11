import RPi.GPIO as GPIO, time
from dataclasses import dataclass

@dataclass
class PWM:
    pin: int
    frequency: float
    duty_cycle: float
    default_state: int = 0
    active: bool = False
    gpio_pwm: GPIO.PWM = None

    name: str = None
    debug: bool = False

    def __post_init__(self):
        if self.debug: print(f"Initializing PWM {self.name if self.name is not None else self.pin}")
        GPIO.setup(self.pin, GPIO.OUT, initial=self.default_state)
        self.gpio_pwm = GPIO.PWM(self.pin, self.frequency)

    def __del__(self):
        if self.debug: print(f"Deleting PWM {self.name if self.name is not None else self.pin}")
        self.stop()
        time.sleep(self.duty_cycle / 100) # Ensure PWM has time to stop
        self.gpio_pwm.stop()
        GPIO.cleanup(self.pin)
        
    def __str__(self) -> str:
        return self.name if self.name != None else f"PWM{self.pin}"
        
    def start(self, duty_cycle: float = None):
        if duty_cycle is not None:
            self.duty_cycle = duty_cycle
            
        if self.debug: print(f"Starting PWM {self.name if self.name is not None else self.pin} with duty cycle {self.duty_cycle}")
        if self.active:
            self.set_duty_cycle(self.duty_cycle)
            return
        self.gpio_pwm.start(self.duty_cycle)
        self.active = True
    
    def on(self):
        self.start()

    def stop(self):
        if self.debug: print(f"Stopping PWM {self.name if self.name is not None else self.pin}")
        self.gpio_pwm.ChangeDutyCycle(0 if self.default_state == 0 else 100)
        self.active = False
        
    def off(self):
        self.stop()
        
    def toggle(self):
        if self.active:
            self.stop()
        else:
            self.start()
        
    def set_frequency(self, frequency: float):
        if self.debug: print(f"Setting PWM frequency for {self.name if self.name is not None else self.pin} to {frequency}")
        self.gpio_pwm.ChangeFrequency(frequency)
        self.frequency = frequency
        
    def set_duty_cycle(self, duty_cycle: float):
        if self.debug: print(f"Setting PWM duty cycle for {self.name if self.name is not None else self.pin} to {duty_cycle}")
        self.gpio_pwm.ChangeDutyCycle(duty_cycle)
        self.duty_cycle = duty_cycle