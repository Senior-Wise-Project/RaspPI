#We will be using the gpiozero library for rasberry pi
from gpiozero import DistanceSensor
from gpiozero import Motor
from Stepper import StepperClass
from time import sleep
from gpiozero import OutputDevice
#This is the set-up code for the distance sensor
'''
echo = 4;
trigger = 5;
sensor = DistanceSensor(echo, trigger)

try:
    # sensor.distance returns the value in meters
    distance_cm = sensor.distance * 100
    print(f"Distance: {distance_cm:.2f} cm")
    sleep(0.5)

except KeyboardInterrupt:
    print("Measurement stopped by user.")
    '''
#----------------------------------------

#This is the set-up code for the DC motor
'''
forward = 4;
backward = 5;
motor = Motor(forward, backward);
#motor.forward() --> moves the motor forward
#motor.backward() --> moves the motor backward
'''
'''
#------------------------------------------------------

#This is the set-up code for the stepper motor
sPin1 = 5;
sPin2 = 6;
sPin3 = 13;
sPin4 = 19;
steps = 2048;
speed = 10;
step_motor1 = StepperClass(steps, sPin1, sPin2, sPin3, sPin4)
step_motor1.set_speed(speed);
step_motor1.step(2048)
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
'''

# BCM GPIO numbers
gpio_numbers = [5, 6, 13, 19]

# Create each GPIO only ONCE
devices = {
    5: OutputDevice(5, initial_value=False),
    6: OutputDevice(6, initial_value=False),
    13: OutputDevice(13, initial_value=False),
    19: OutputDevice(19, initial_value=False),
}

possible_orders = [
    [5, 6, 13, 19],
    [5, 13, 6, 19],
    [5, 6, 19, 13],
    [5, 19, 6, 13],
    [5, 13, 19, 6],
    [5, 19, 13, 6],
]

half_step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

def all_off():
    for device in devices.values():
        device.off()

try:
    for order in possible_orders:
        print("Trying GPIO order:", order)

        pins = [devices[gpio] for gpio in order]

        for i in range(256):
            for step in half_step_sequence:
                for pin, value in zip(pins, step):
                    pin.value = value
                sleep(0.01)

        all_off()
        sleep(2)

except KeyboardInterrupt:
    pass

finally:
    all_off()
    for device in devices.values():
        device.close()

'''
def rotateBase(angle):
    step = int(2048/360*angle)
    step_motor1.step(step)

def rotateBarrel(angle):
    step = int(2048/360*angle)
    step_motor2.step(step)

'''