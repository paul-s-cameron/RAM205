from time import sleep
from RPiC.Rover import Rover

rover = Rover(debug=True)

rover.buzzer.start()

sleep(3)

rover.buzzer.stop()