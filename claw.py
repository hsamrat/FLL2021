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
        self.claw.reset()
        while True:
            self.claw.on_for_rotations(10, 0.02, brake = False)
            if 'stalled' in self.claw.state:
                #init.debug_print(self.claw.state)
                break




    def claw_close(self, percent):
        i = 0
        self.claw.reset()
        while True:

            self.claw.on_for_rotations(10, 0.02, brake = False)

            if 'stalled' in self.claw.state:
                #init.debug_print(self.claw.state)
                break

            i += 1
        #init.debug_print(i)
        self.claw.on_for_rotations(10, 0.02, brake = True)

        if i <= 5:
            print("caught brick")
            return True

        else:
            return False

    def claw_close_5(self):
        i = 0
        self.claw.reset()
        while True:

            self.claw.on_for_rotations(-10, 0.01, brake = False)

            if 'stalled' in self.claw.state:
                #init.debug_print(self.claw.state)
                break

            i += 1
        #init.debug_print(i)
        self.claw.on_for_rotations(-10, 0.02, brake = True)

        if i <= 15:
            return "Has Nothing"
        if i <= 23:
            #init.debug_print("caught brick")
            return "caught brick"

        else:
            #init.debug_print("Has Nothing")
            return "Has Nothing"


        return


