#!/usr/bin/env python3

import ev3dev.ev3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound
import init
import claw

my_tank = MoveTank(OUTPUT_A, OUTPUT_B)
lift = MediumMotor(OUTPUT_D)
claw = claw.Claw()
claw.claw.reset()
 # Init Color Sensors

colorRight = ColorSensor(INPUT_2)

colorLeft = ColorSensor(INPUT_3)


#Moving the Robot
if claw.claw_close(100):
    #holding somethigng
else:
    # not holding
'''
lift.on_for_rotations(49, -3)
sleep(0.2)
my_tank.on_for_rotations(20, 20, -.5)
my_tank.on_for_rotations(20, 0, 0.8)
my_tank.on_for_rotations(20, 20, 0.8)
sleep(1)
lift.on_for_rotations(49, 2.5)

claw.claw_open(100)
# lift.on_for_rotations(49, -3)
# my_tank.on_for_rotations(20, 20, -0.6)
# my_tank.on_for_rotations(-15, 15, 0.43)
# my_tank.on_for_rotations(20, 20, 0.5)
# lift.on_for_rotations(-49, 3)

# claw.claw_close(100)



# lift.on_for_rotations(49, 3)

# my_tank.on_for_rotations(10, 10, -.55)
# my_tank.on_for_rotations(15, -15, 0.43)
# my_tank.on_for_rotations(15, 15, 0.5)
# lift.on_for_rotations(49, 3)


# claw.claw_close(100)
'''
