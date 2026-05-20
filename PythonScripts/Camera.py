from time import sleep
from picamera2 import Picamera2
from pathlib import Path

camera = Picamera2()
#-----------------------------------
# What you write:
    #camera = picamera.PiCamera()

    # What the Pi actually hears:
    #camera = picamera.PiCamera(camera_num=0)
#Max resolution: 2592 x 1944
#------------------------------------
camera.configure(camera.create_still_configuration())
camera.start()
# Give the sensor 2 seconds to adjust exposure, white balance, and focus
sleep(2)
imagePath = Path.cwd().parent / Path('Images') / Path('image.jpg')
camera.capture_file(imagePath)
camera.stop()
print("Image captured successfully!")
#the camera finishes adjusting during these 2 seconds


#Grabs an absolute path that works for all operating systems as well as for any computer b/c of it using relative paths.