#link to website where inital code was from: https://www.explainingcomputers.com/sample_code/Servo_Test_CC_Go_to_Angle.py

# we need to add the camera module and PIR Sensor code


# Import libraries
import RPi.GPIO as GPIO
import time

  
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)


def cleaning_things_at_the_end():
  #Clean things up at the end
  servo1.stop()
  GPIO.cleanup()
  print("Goodbye!")
  
# defining the movement (90 degrees clockwise)
# time statment can be anything
# ChangeDutyCycle = 0 removes jitters by servo motor
# adding 2 is necessary
def moving_motor_90_clockwise():
  servo1.ChangeDutyCycle(2+(90/18))
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)
  
'''defining the movement (90 degrees anti-clockwise)'''
# time statment can be anything
# ChangeDutyCycle = 0 removes jitters by servo motor
# adding 2 is necessary
def moving_motor_90_anti_clockwise():
  servo1.ChangeDutyCycle(2+(90/18))
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)
  
  

# moving_motor_90_clockwise():
# moving_motor_90_anti_clockwise():
cleaning_things_at_the_end()



