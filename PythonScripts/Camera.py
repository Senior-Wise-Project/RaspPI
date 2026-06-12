from time import sleep
#from picamera2 import Picamera2
from pathlib import Path
import cv2
import numpy as np
import os
import Mechanics

absoluteCenter = (1, 1)
isAligned = False
x_min = 0
x_max = 0
y_min = 0
y_max = 0
height = 960
width = 1440
tolerance_px = 0


def alignCameraHorizontally():
    global height, width, x_max, x_min, absoluteCenter
    np = 0.01
    cx = width/2
    tx = absoluteCenter[0]
    angle = np*(cx-tx)
    if(tx > x_min and tx < x_max):
        return
    else:
        Mechanics.rotateBase(angle)
        absoluteCenter = detectCenter()
        if(absoluteCenter == None):
            return
        alignCameraHorizontally()

    print("Aligned!")


def alignCameraVertically():
    global height, width, x_max, x_min, absoluteCenter
    np = 0.01
    cx = width / 2
    tx = absoluteCenter[0]
    angle = np * (cx - tx)
    if (tx > y_min and tx < y_max):
        return
    else:
        Mechanics.rotateBarrel(angle)
        absoluteCenter = detectCenter()
        if (absoluteCenter == None):
            return
        alignCameraVertically()

#Precondition: The camera is already aligned

#angle1 is less than angle 2
def lookAround(angle1, angle2):
    Mechanics.rotateBarrel(-Mechanics.getVertcalAngle()/2)
    currAngle = Mechanics.getHorizontalAngle()
    angle = 2

    while(detectCenter() == None):
        if(currAngle+angle>= angle2 or currAngle+angle<=angle1):
            angle *= -1
            Mechanics.rotateBarrel(5)
        Mechanics.rotateBase(angle)
        currAngle+=angle
    return



def check_camera_alignment(target_center, frame):
    global x_min, y_min, x_max, y_max, tolerance_px
    """
    Determines if the target center is aligned with the camera center.
    Also draws a visual cue box onto the frame.

    :param target_center: tuple (x, y) of the detected target's center
    :param frame: the current OpenCV frame image
    :param tolerance_px: how many pixels out from absolute center the target can drift
    :return: Boolean (True if aligned, False if not)
    """
    # If no target was found in the frame, we are obviously not aligned
    if target_center is None:
        return False

    # 1. Grab camera dimensions and calculate absolute center
    height, width = frame.shape[:2]
    cam_cx, cam_cy = width // 2, height // 2
    print("EEEEE")
    print(height)
    print(width)

    # 2. Define the boundary thresholds for your alignment box
    x_min, x_max = cam_cx - tolerance_px, cam_cx + tolerance_px
    y_min, y_max = cam_cy - tolerance_px, cam_cy + tolerance_px

    # 3. Unpack your target coordinates
    target_x, target_y = target_center

    # 4. Check if the target center is inside the threshold box
    is_aligned = (x_min <= target_x <= x_max) and (y_min <= target_y <= y_max)

    # 5. Visual Feedback: Cyan if locked on, Red if misaligned
    box_color = (255, 255, 0) if is_aligned else (0, 0, 255)

    # Draw the tolerance box
    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), box_color, 2)

    # Draw a tiny crosshair at the exact pixel center of the camera
    cv2.drawMarker(frame, (cam_cx, cam_cy), (255, 255, 255), cv2.MARKER_CROSS, 10, 1)

    return is_aligned


def detectCenter():
    global absoluteCenter
    global isAligned
    imagePath = Path.cwd().parent / Path('Images') / Path("image.jpg")
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

    #draws all valid circles in most circular order
    for i in range(len(valid_circles)):
        score, center, radius = valid_circles[i]
        if (i == 0):
            absoluteCenter = center
        print(f"🎯 Dartboard detected! Circularity Match: {score:.2f}")
        print(center)
        cv2.circle(img, center, radius, (0, 255, 0), 3)
        cv2.circle(img, center, 2, (0, 0, 255), 3)

    #Grabs the center of the most circular object
    if len( valid_circles) != 0:
        center= valid_circles[0][1]
        print(center)
        return center
    else:
        return None

    '''
        isAligned = check_camera_alignment(absoluteCenter, img)
        print(isAligned)
    
    destination = Path.cwd().parent / Path('Images') / Path("processedImage.jpg")
    # 3. Safety check: Create the folder if it doesn't exist yet
    os.makedirs(destination.parent, exist_ok=True)

    cv2.imwrite(destination, img)




    cv2.imshow("Best Geometric Circle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''


detectCenter()
print("EEEEEEEEE")
print(absoluteCenter)

'''
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

'''