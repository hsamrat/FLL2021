from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_D, OUTPUT_A, SpeedPercent, follow_for_ms, SpeedRPM, LargeMotor, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor
from time import sleep
from ev3dev2.sound import Sound
import init

class Claw():
    def __init__(self):
        self.claw = MediumMotor(OUTPUT_C)

    def claw_open(self, percent):
        rotations = 3 * (percent/100)
        self.claw.on_for_rotations(50, 3)

    def claw_close(self, percent):
        rotations = 2.9 * (percent/100)
        self.claw.on_for_rotations(-50, 3.0)

    # def claw_open(self, percent):
    #     rotations = 3 * (percent/100)
    #     self.claw.on_for_rotations(50, rotations)

    # def claw_close(self, percent):
    #     rotations = 2.9 * (percent/100)
    #     self.claw.on_for_rotations(-50, rotations)


