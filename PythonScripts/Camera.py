from time import sleep
from picamera2 import Picamera2
from pathlib import Path
import cv2
import numpy as np
import os

def detectCenter():
    imagePath = Path('/home/wiseproject/Images/image.jpg')
    if not os.path.exists(imagePath.parent):
        os.makedirs(imagePath.parent)
    img1 = cv2.imread(imagePath)
    if img1 is None:
        print("Failed to load image")
        return
    img = img1.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 1. Use Canny Edge Detection to find all outlines
    edges = cv2.Canny(blurred, 50, 150)

    # 2. Find the contours (the continuous lines) of those shapes
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    valid_circles = []

    #infinite loop?
    for cnt in contours:
        # Calculate area and perimeter
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)

        # Skip tiny speckles or division-by-zero errors
        if area < 100 or perimeter == 0:
            continue

        # Apply the circularity formula: (4 * pi * Area) / (Perimeter^2)
        circularity = (4 * np.pi * area) / (perimeter ** 2)

        # If it's highly circular (e.g., matching better than 85% of a perfect circle)
        if circularity > 0.85:
            # Get bounding circle data to use for drawing later
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)

            # Save the circle along with its score
            valid_circles.append((circularity, center, radius))

    # 3. SORT the list so the highest circularity score (closest to 1.0) is FIRST
    valid_circles.sort(key=lambda item: item[0], reverse=True)
    # 4. Draw only the absolute best, most perfect circle found

    for i in range(len(valid_circles)):
        score, center, radius = valid_circles[i]
        print(f"🎯 Dartboard detected! Circularity Match: {score:.2f}")
        cv2.circle(img, center, radius, (0, 255, 0), 3)
        cv2.circle(img, center, 2, (0, 0, 255), 3)

    #Grabs the center of the most circular object
    ''''
    if len( valid_circles) == 0:
        center= valid_circles[0][1]
        print(center)
        return center
    else:
        return None
    '''
    destination = Path.cwd().parent / Path('Images') / Path("processedImage.jpg")
    # 3. Safety check: Create the folder if it doesn't exist yet
    os.makedirs(destination.parent, exist_ok=True)

    cv2.imwrite(destination, img)



    #cv2.imshow("Best Geometric Circle", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

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
imagePath = Path('/home/wiseproject/Images/image.jpg')
camera.capture_file(imagePath)
camera.stop()
print("Image captured successfully!")
detectCenter()
#the camera finishes adjusting during these 2 seconds


#Grabs an absolute path that works for all operating systems as well as for any computer b/c of it using relative paths.