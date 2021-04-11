#First, import the RPi.GPIO library and the sleep function.
import RPi.GPIO as GPIO
from time import sleep

#Then, setup the GPIO mode as BOARD so that you can reference the PINs and not the BCM pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

#Next, create a variable for the servo. I called mine “PWM.” Then, send a 50 Hz PWM signal on that GPIO pin using the GPIO.PWM() function. Start the signal at 0.
pwm=GPIO.PWM(11, 50)
pwm.start(0)

# Use the ChangeDutyCycle() function to write duty cycle percentages to the servo motor. 
pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(1)
pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)

#Lastly, clean up the code by stopping the PWM signal and running the cleanup function on the GPIO pins.

pwm.stop()
GPIO.cleanup()
