#https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/
- #where I got my code from 
#https://drive.google.com/file/d/1vy77kxSVM_PSUzkhrlFFGU6p4DDUlGNo/view?usp=drivesdkhttps://drive.google.com/file/d/1vy77kxSVM_PSUzkhrlFFGU6p4DDUlGNo/view?usp=drivesdk

  
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

#Now, you can create a Python function based on this formula to calculate the duty cycle percentage based on a given angle.


def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
