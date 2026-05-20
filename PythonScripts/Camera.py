from time import sleep
from picamera import PiCamera
from pathlib import Path

camera = PiCamera()
#-----------------------------------
# What you write:
    #camera = picamera.PiCamera()

    # What the Pi actually hears:
    #camera = picamera.PiCamera(camera_num=0)
#Max resulotion: 2592 x 1944
#------------------------------------
camera.resolution = (1024, 768)
camera.start_preview()
#The camera turns on, the preview appears, and AE/AWB start calibrating.
sleep(2)
#the camera finishes adjusting during these 2 seconds

imagePath = Path.cwd().parent / Path('Images') / Path('image.jpg')
#Grabs an absolute path that works for all operating systems as well as for any computer b/c of it using relative paths.
print(imagePath)
#camera.capture(imagePath)