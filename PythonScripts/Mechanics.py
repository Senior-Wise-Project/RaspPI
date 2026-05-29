#We will be using the gpiozero library for rasberry pi
from gpiozero import DistanceSensor
from gpiozero import Motor
from Stepper import StepperClass
from time import sleep
#This is the set-up code for the distance sensor
echo = 4;
trigger = 5;
sensor = DistanceSensor(echo, trigger)
try:
    while True:
        # sensor.distance returns the value in meters
        distance_cm = sensor.distance * 100
        print(f"Distance: {distance_cm:.2f} cm")
        sleep(0.5)

except KeyboardInterrupt:
    print("Measurement stopped by user.")
#----------------------------------------

#This is the set-up code for the DC motor
forward = 4;
backward = 5;
motor = Motor(forward, backward);
#motor.forward() --> moves the motor forward
#motor.backward() --> moves the motor backward
#------------------------------------------------------

#This is the set-up code for the stepper motor
sPin1 = 16;
sPin2 = 12;
sPin3 = 6;
sPin4 = 13;
steps = 2048;
speed = 10;
step_motor = StepperClass(steps, sPin1, sPin2, sPin3, sPin4)
step_motor.set_speed(speed);
s2Pin1 = 17;
s2Pin2 = 27;
s2Pin3 = 22;
s2Pin4 = 23;
steps = 2048;
speed = 10;
step_motor2 = StepperClass(steps, s2Pin1, s2Pin2, s2Pin3, s2Pin4)
step_motor2.set_speed(speed);
#step_motor.step(1024) rotates the stepper motor halfway
#step_motor.step(-1024) rotates the stepper motor halfway in the other direction


