from time import sleep
from RPiC.Rover import Rover

rover = Rover(debug=True)

rover.warner.start()

sleep(5)

rover.warner.set_frequency(8)

sleep(5)

rover.warner.stop()