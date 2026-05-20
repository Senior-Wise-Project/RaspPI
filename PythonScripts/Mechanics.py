#We will be using the gpiozero library for rasberry pi
from gpiozero import DistanceSensor
from gpiozero import Motor
from gpiozero import Stepper
from time import sleep


#This is the set-up code for the distance sensor
dPin1 = 23;
dPin2 = 24;
sensor = DistanceSensor(dPin1, dPin2)
distance = sensor.distance()
#----------------------------------------

#This is the set-up code for the DC motor
forward = 4;
backward = 5;
motor = Motor(forward, backward);
#motor.forward() --> moves the motor forward
#motor.backward() --> moves the motor backward
#------------------------------------------------------

#This is the set-up code for the stepper motor
sPin1 = 1;
sPin2 = 2;
sPin3 = 3;
sPin4 = 4;
steps = 2048;
speed = 10;
step_motor = Stepper(steps, sPin1, sPin2, sPin3, sPin4)
step_motor.set_speed(speed);
#step_motor.step(1024) rotates the stepper motor halfway
#step_motor.step(-1024) rotates the stepper motor halfway in the other direction


