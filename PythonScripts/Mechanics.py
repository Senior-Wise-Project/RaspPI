#We will be using the gpiozero library for rasberry pi
from gpiozero import DistanceSensor
from gpiozero import Motor
#from Stepper import StepperClass
from time import sleep
from gpiozero import OutputDevice
from gpiozero import LED
#This is the set-up code for the distance sensor
from gpiozero import LED
from gpiozero import PWMOutputDevice

''' 
echo = 4;
trigger = 5;
sensor = DistanceSensor(echo, trigger)
currBarrAngle = 0
'''

#CHANGE THIS VALUE
'''
motor = PWMOutputDevice(12)

#power ranges from 0.1 to 1.0
def shoot(power):
    motor.value = power
    sleep(3)
    motor.value = 0.0
    print("power off")
    sleep(0.5)

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

#motor.forward() --> moves the motor forward
#motor.backward() --> moves the motor backward

#------------------------------------------------------

#This is the set-up code for the stepper motor
'''
'''
sPin1 = 15;
sPin2 = 25;
sPin3 = 6;
sPin4 = 8;
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

#shoot(1)   
'''
# 1. SETUP: Match this to the pin layout that worked for you!
barrel_motor_pins = [15, 25, 6, 8]
barrelPins = [OutputDevice(pin) for pin in barrel_motor_pins]
base_motor_pins = [17, 27, 22, 23]
basePins = [OutputDevice(pin) for pin in base_motor_pins]
# Standard 4-step sequence
sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]


# 2. THE METHOD
def rotateBase(degrees, speed=0.01):
    global basePins
    pins = basePins
    """
    Rotates the stepper motor by a specified number of degrees.
    Positive degrees = Clockwise
    Negative degrees = Counter-Clockwise
    """
    # Calculate the total number of steps required
    steps_needed = int(abs(degrees) * 2048 / 360)

    # Choose direction by reversing the step sequence if degrees are negative
    if degrees >= 0:
        step_sequence = sequence
    else:
        step_sequence = sequence[::-1]  # Reverses the array for CCW

    print(f"Rotating {degrees}° ({steps_needed} steps)...")

    # Execute the steps
    for step_count in range(steps_needed):
        # The % 4 operator keeps cycling through our 4-step sequence repeatedly
        current_step = step_sequence[step_count % 4]

        for i in range(4):
            if current_step[i] == 1:
                pins[i].on()
            else:
                pins[i].off()
        sleep(speed)

    # Safety feature: Turn off all pins when done so the motor doesn't get hot
    for pin in pins:
        pin.off()

def rotateBarrel(degrees, speed=0.01):
    global barrelPins
    pins = barrelPins
    """
    Rotates the stepper motor by a specified number of degrees.
    Positive degrees = Clockwise
    Negative degrees = Counter-Clockwise
    """
    # Calculate the total number of steps required
    steps_needed = int(abs(degrees) * 2048 / 360)

    # Choose direction by reversing the step sequence if degrees are negative
    if degrees >= 0:
        step_sequence = sequence
    else:
        step_sequence = sequence[::-1]  # Reverses the array for CCW

    print(f"Rotating {degrees}° ({steps_needed} steps)...")

    # Execute the steps
    for step_count in range(steps_needed):
        # The % 4 operator keeps cycling through our 4-step sequence repeatedly
        current_step = step_sequence[step_count % 4]

        for i in range(4):
            if current_step[i] == 1:
                pins[i].on()
            else:
                pins[i].off()
        sleep(speed)

    # Safety feature: Turn off all pins when done so the motor doesn't get hot
    for pin in pins:
        pin.off()



# 3. TEST EXAMPLES
try:
    # Rotate 90 degrees clockwise
    rotateBarrel(60)
    sleep(1)
    rotateBase(60)

    # Rotate a full 360 degrees counter-clockwise
    rotateBarrel(-60)
    sleep(1)
    rotateBase(-10)

    # Rotate 45 degrees clockwise slightly faster
    rotateBarrel(45, speed=0.006)
    rotateBase(45, speed = 0.006)
except KeyboardInterrupt:
    print("\nCleaning up...")
    for pin in barrelPins:
        pin.off()
    for pin in basePins:
        pin.off()

