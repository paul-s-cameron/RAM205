import RPi.GPIO as GPIO

class TrackSensor():
    Sensor1: int
    Sensor2: int
    Sensor3: int
    Sensor4: int
    debug: bool = False
    
    def __init__(self, sensor1=3, sensor2=5, sensor3=4, sensor4=18, debug=False):
        self.Sensor1, self.Sensor2, self.Sensor3, self.Sensor4 = sensor1, sensor2, sensor3, sensor4
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            
        GPIO.setup(self.Sensor1, GPIO.IN)
        GPIO.setup(self.Sensor2, GPIO.IN)
        GPIO.setup(self.Sensor3, GPIO.IN)
        GPIO.setup(self.Sensor4, GPIO.IN)
        
        self.debug = debug
        
    def __del__(self):
        GPIO.cleanup([self.Sensor1, self.Sensor2, self.Sensor3, self.Sensor4])
        
    def get_values(self):
        """ Get track sensor values

        Returns:
            _list_: _bool_ [Sensor1, Sensor2, Sensor3, Sensor4]
        """
        if self.debug: print("Getting track sensor values")
        value_list = []
        value_list.append(GPIO.input(self.Sensor1) == GPIO.HIGH)
        value_list.append(GPIO.input(self.Sensor2) == GPIO.HIGH)
        value_list.append(GPIO.input(self.Sensor3) == GPIO.HIGH)
        value_list.append(GPIO.input(self.Sensor4) == GPIO.HIGH)
        if self.debug: print(value_list)
        return value_list