#link to website where inital code was from: https://www.explainingcomputers.com/sample_code/Servo_Test_CC_Go_to_Angle.py



# Import libraries
import RPi.GPIO as GPIO
import time
def cleaning_things_at_the_end():
  #Clean things up at the end
  servo1.stop()
  GPIO.cleanup()
  print("Goodbye!")
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

servo1.ChangeDutyCycle(2+(angle/18))
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
cleaning_things_at_the_end()



