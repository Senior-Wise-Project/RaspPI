#We will be using the gpiozero library for rasberry pi
from gpiozero import DistanceSensor
from gpiozero import Motor
from Stepper import StepperClass
from time import sleep
from gpiozero import OutputDevice
from gpiozero import LED
#This is the set-up code for the distance sensor
from gpiozero import LED
from gpiozero import PWMOutputDevice

echo = 4;
trigger = 5;
sensor = DistanceSensor(echo, trigger)
currBarrAngle = 0

#CHANGE THIS VALUE
motor = PWMOutputDevice(18)

#power ranges from 0.1 to 1.0
def shoot(power):
    motor.value = power
    sleep(3)
    motor.value = 0.0

def findAverageDistance():
    # sensor.distance returns the value in meters
    total = 0
    for i in range(10):
        distance_cm = sensor.distance * 100
        total += distance_cm
        sleep(0.5)
    return total/10

def getVerticalAngle():
    steps = step_motor2.step_number
    return steps/step_motor2.number_of_steps * 360
#----------------------------------------

def getHorizontalAngle():
    steps = step_motor1.step_number
    return steps / step_motor2.number_of_steps * 360
#This is the set-up code for the DC motor

forward = 4;
backward = 5;
motor = Motor(forward, backward);
#motor.forward() --> moves the motor forward
#motor.backward() --> moves the motor backward

#------------------------------------------------------

#This is the set-up code for the stepper motor
'''
sPin1 = 5;
sPin2 = 6;
sPin3 = 13;
sPin4 = 19;
steps = 2048;
speed = 10;
step_motor1 = StepperClass(steps, sPin1, sPin2, sPin3, sPin4)
step_motor1.set_speed(speed);
step_motor1.step(2048)
'''
s2Pin1 = 17;
s2Pin2 = 27;
s2Pin3 = 22;
s2Pin4 = 23;
steps = 2048;
speed = 10;
step_motor2 = StepperClass(steps, s2Pin1, s2Pin2, s2Pin3, s2Pin4)
step_motor2.set_speed(speed);
step_motor2.step(2048)
#step_motor.step(1024) rotates the stepper motor halfway
#step_motor.step(-1024) rotates the stepper motor halfway in the other direction



def rotateBase(angle):
    step = int(2048/360*angle)
    step_motor1.step(step)

def rotateBarrel(angle):
    step = int(2048/360*angle)
    step_motor2.step(step)

