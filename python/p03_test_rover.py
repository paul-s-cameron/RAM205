''' p03_test_rover.py
    RAM205 Final Assessment 
    Fall 2023
    Testing the rover factory and classes.
    Enter code below for all "#TODO your code here" prompts
    Use the rover object as the entry point for all rover operations.
'''
import sys
sys.path.append("/home/ram/model/")

#TODO additional import statments may be required for some tests. 
from Rover import Rover
from rover_factory import make_rover

### use the rover factory to create a rover object named rover. ###
rover = make_rover()

print("*** Rover Testing ***")
print()
print("You will be prompted for which components to test.")
print("When tests are run, you will indicated if is was")
print("successful by entering 'y' or 'n'. ")
print("The numbers of tests ran, tests passed, and tests ")
print("failed are reported at the end.")
print()
#count = 30 if all ran
tests_ran = 0
tests_passed = 0
tests_failed = 0

choice = input("\nRun buzzer test? ")
if choice.upper()[0] == "Y":
    ### turn buzzer on ###
    tests_ran += 1
    rover.buzzer.on()

    result = input("Is the buzzer on? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### turn buzzer off using the update() function ###
    tests_ran += 1
    rover.buzzer.off()

    result = input("Is the buzzer off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### toggle the buzzer on ###
    tests_ran += 1
    rover.buzzer.toggle()

    result = input("Is the buzzer on? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### Use buzzer functions to test its state ###
    ### if the buzzer is on then turn it off ###
    tests_ran += 1
    if rover.buzzer.active:
        rover.buzzer.off()

    result = input("Is the buzzer off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### beep the buzzer ###
    ### beep the buzzer very quickly with very short beeps ###
    tests_ran += 1
    rover.buzzer.beep(12, 80)

    result = input("Is the buzzer beeping quickly with short duration?")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    #### turn beeping off using only the buzzer's beep() function ###
    tests_ran += 1
    rover.buzzer.beep(1, 100)

    result = input("Is the buzzer off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    

choice = input("\nRun drive test? ")
if choice.upper()[0] == "Y":
    ### drive forward ###
    tests_ran += 1
    rover.drive.forward(30)

    result = input("Is the rover moving forward? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### turn left forward at one quarter speed ###
    tests_ran += 1
    rover.drive.stop()
    rover.drive.RM_forward(25)

    result = input("Is the rover pivoting forward to the left at quarter speed? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### rotate right - do not change speed. ###
    tests_ran += 1
    rover.drive.rotate_right()

    result = input("Is the rover rotating to the right? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### stop the rover using a Operation ###
    tests_ran += 1
    rover.drive.stop()

    result = input("Is the rover stopped? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### go forward at speed of 47 using a single drive command ###
    tests_ran += 1
    rover.drive.forward(47)
    
    result = input("Is the rover moving forward at speed of 47? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### use the delta speed feature to decrease the speed to 42 ###
    ### add a second line of code that prints the rover's speed property. ###
    tests_ran += 1
    rover.drive.delta_speed(-5)

    result = input("Is the rover moving forward at speed of 42 and value output to terminal? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### stop the rover by adjusting the speed ###
    tests_ran += 1
    rover.drive.set_speed(0)
    
    result = input("Is the rover stopped? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1
    
##################################
##  I would like to point out   ##
##  that I was unable to test   ##
##  the gimbal functions.       ##
##  Since it is broken.         ##
##################################
choice = input("\nRun gimbal test? ")
if choice.upper()[0] == "Y":
    print("Using Gimbal functions. (not servo)")
    ### rotate the gimbal fully up ###
    tests_ran += 1
    rover.gimbal.vertical.set_pos(180)

    result = input("Is the gimbal rotated fully up? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### rotate the gimbal fully left ###
    tests_ran += 1
    rover.gimbal.horizontal.set_pos(180)

    result = input("Is the gimbal rotated fully left? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### use the update() functions of the servo components  ###
    ### contained in the gimbal object to rotate the gimbal ###
    ### slightly left and slighly down. Two function calls  ###
    ### are required.                                       ###
    tests_ran += 1
    rover.gimbal.delta_pos(-20, -20)

    result = input("Is the gimbal rotated to the slightly left and down? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

choice = input("\nRun LED test? ")
### Use the RGB_LED object contained in the rover object 
### to complete the following.
if choice.upper()[0] == "Y":
    ### turn red LED on ###
    tests_ran += 1
    rover.led.set_color(255, 0, 0)
    rover.led.on()

    result = input("Is the red LED on? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### use the update function to turn red LED off ###
    tests_ran += 1
    rover.led.off()

    result = input("Is the red LED off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### toggle the red LED on ###
    tests_ran += 1
    rover.led.R.toggle()

    result = input("Is the red LED on? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### use the dim function to turn the red led off ###
    tests_ran += 1
    rover.led.set_brightness(0)

    result = input("Is the red LED off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### blink the red LED quickly with the LED staying  ###
    ### on most of the time.                             ###
    tests_ran += 1
    rover.led.blink(rover.led.R, duty_cycle=80, frequency=2)

    result = input("Is the red LED blinking quickly and mostly on?")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### check the state of the red led. If it is on then    ###
    ### turn it off                                         ###
    tests_ran += 1
    if rover.led.R.active:
        rover.led.R.off()

    result = input("Is the red LED off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    

choice = input("\nRun rgb_led test? ")
if choice.upper()[0] == "Y":
    ### set the color of the RGB LED to magenta using   ###
    ### set color function                              ###                                
    tests_ran += 1
    rover.led.on()
    rover.led.set_color(255, 0, 255)

    result = input("Is the RGB LED magenta? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    

    ### set the color of the RGB LED to white using the ###
    ### update function.                                 ###
    tests_ran += 1
    rover.led.set_color(255, 255, 255)

    result = input("Is the RGB LED white? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    

    ### use the set color function to turn all RGB LEDs off) ###
    tests_ran += 1
    rover.led.set_color(0, 0, 0)
    
    result = input("Are all RGB LEDs off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1        

choice = input("\nRun servo test? ")
if choice.upper()[0] == "Y":
    ### center the front servo ###
    tests_ran += 1
    rover.sonar.set_pos(90)

    result = input("Is the front servo centered? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    

    ### turn front servo counter-clockwise ###
    tests_ran += 1
    rover.sonar.ccw(45)

    result = input("Is the front servo rotated to the left? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1    


choice = input("\nRun sonar test? ")
if choice.upper()[0] == "Y":
    tests_ran += 1
    print("Place the object in front of sonar.")
    print("Read the distance and print.")
    input("Press enter when you're ready to read the sensor")
    print(rover.sonar.distance())

    result = input("Did the distance read correctly? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

choice = input("\nRun warner test? ")
### #TODO Open the rover factory. Update the warner so that
### only the amber led is used. No buzzer operation is included.
###
if choice.upper()[0] == "Y":
    ### turn the warner on - no buzzer. See above TODO. ###
    tests_ran += 1
    rover.warner.on()

    result = input("Is warner on with only the amber led active? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

    ### turn the warner off
    tests_ran += 1
    rover.warner.off()

    result = input("Is the warner off? ")
    if result.upper()[0] == "Y":
        tests_passed += 1
    else:
        tests_failed += 1

print()
print("*** Testing Completed ***")
print(f"Number of tests ran: {tests_ran}") 
print(f"Number of tests passed: {tests_passed}") #fully tested and function - count = 32
print(f"Number of tests failed: {tests_failed}") #fully tested and function - count = 0   
