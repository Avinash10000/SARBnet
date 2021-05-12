
'''Open In Colab
Step 2: Running The CNN on the Raspberry Pi4B
Requirements
Run the list below and solve any dependency errors using sudo apt-get {module}'''


'''Constants'''
#These are the constant values needed for the whole code to function.

#name the temporary image path
TEMP_IMG_PATH = "img.jpg"

#directory to store images that have been classified
STORE_DIRECTORY = "Classified_Images"


#input dimensions for the images
WIDTH = 64
HEIGHT = 64
CHANNELS=3


#these are the list of classes that we have 
CLASS_LIST = ['cardboard', 'compost', 'glass', 'metal', 'paper', 'plastic', 'trash']
''' need to change the next three'''
COMPOST_LIST = ['compost']
TRASH_LIST = ['trash']
CARDBOARD_LIST = ['cardboard']
GLASS_LIST = ['glass']
METAL_LIST = ['metal']
PAPER_LIST = ['paper']
PLASTIC_LIST = ['plastic']
'''Taking the Picture and PiCamera/PIR Sensor/Servo Motor Code'''

from time import sleep
import cv2
 
import os
import tensorflow as tf
import keras
from keras.models import load_model

from glob import glob




# Import libraries
import RPi.GPIO as GPIO
import time

import numpy as np
import io
from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image as Img
''' need to add PIR part'''
import picamera
import picamera.array

camera = PiCamera()
stream=PiRGBArray(camera)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.IN)
num=1

#load the pretrained model
model = keras.models.load_model("trained_model.h5")

def scale_X(X):
    
    return X/255.0

#preprocess the image given to be classified
def process_single_img(image):
    # img = cv2.imread(TEMP_IMG_PATH)
    #resize and normalize images
    if CHANNELS==1:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (WIDTH, HEIGHT))
    image = scale_X(image)
    image = image.reshape(WIDTH,HEIGHT,CHANNELS)
    return image

#predicts a single image given the numpy array of the image
def predict_single_img(image):
    #preprocesss the image
    processed_img = process_single_img(image)

    #predict the image using the preloaded model
    prediction = model.predict(np.array([processed_img]))
    pred = np.argmax(prediction)

    print(pred)
    #match the numerica predicted class to the name
    pred_class = CLASS_LIST[pred]
    print(pred_class)
    
    #sort into trash, recycling or compost
    waste_type = "trash"
    if pred_class in COMPOST_LIST:
        waste_type = "compost"
    elif pred_class in METAL_LIST:
        waste_type= "metal"
    elif pred_class in CARDBOARD_LIST:
        waste_type = 'cardboard'
    elif pred_class in GLASS_LIST:
        waste_type = 'glass'
    elif pred_class in PAPER_LIST:
        waste_type = 'paper'
    elif pred_class in PLASTIC_LIST:
        waste_type = 'plastic'
    return (waste_type , pred_class)



#store the specific given waste type in the appropriate folder with
#an enumerated name    
def store_in_folder(waste_type):
	parent_dir = STORE_DIRECTORY+"/"+waste_type+"/"
	num = len(glob(parent_dir+"*.jpg"))
	print("current num images:",num)
	os.rename(TEMP_IMG_PATH, parent_dir+waste_type +str(num+1)+".jpg")


def pir_sensor():
    
    while GPIO.input(11)==0:
        time.sleep(0.5)
    else:
         
        camera.capture(stream, format="bgr")
        image = stream.array
        cv2.imwrite(TEMP_IMG_PATH,image)
        sleep(1)
        camera.stop_preview()
        stream.truncate(0)
        predict_single_img(image)
        return (image, waste_type)        
pir_sensor()                     
 

  
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 12 as an output, and define as servo1 as PWM pin
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50) # pin 11 for servo1, pulse 50Hz

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
def moving_item_to_left():
    servo1.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    time.sleep(3.5)
    servo1.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
  
  
'''defining the movement (90 degrees anti-clockwise)'''
# time statment can be anything
# ChangeDutyCycle = 0 removes jitters by servo motor
# adding 2 is necessary
def moving_item_to_right():
    servo1.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)





if pred_class == 'cardboard' or 'trash' or 'glass' or 'paper' or 'plastic':
  moving_item_to_left()
  cleaning_things_at_the_end()
elif pred_class == 'compost' or 'trash':
  moving_item_to_right()
  cleaning_things_at_the_end()
