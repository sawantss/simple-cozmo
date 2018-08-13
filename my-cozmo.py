'''
This class can be used as template for cozmo programs.
'''

import time

from cozmo.robot import Robot
import cozmo
from cozmo.lights import green_light, red_light, white_light, blue_light, off_light

from simple.wrapper import SimpleRobot

__author__ = "Shitalkumar Sawant"
__copyright__ = "Copyright(c) 2018 All rights reserved"


def hello_world_cozmo(robot: Robot):
    simple = SimpleRobot(robot)
    #Add your code here


cozmo.run_program(hello_world_cozmo)