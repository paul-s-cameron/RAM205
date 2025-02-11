from time import sleep
from RPiC.Rover import Rover

rover = Rover(debug=True)

rover.led.on()

sleep(1)

rover.led.set_color(0, 255, 0)

sleep(1)

rover.led.blink(rover.led.B, duty_cycle=80, frequency=2)

sleep(3)

rover.led.set_color(255, 0, 0)
rover.led.set_brightness(20)

sleep(2)

rover.led.off()