'''
This has examples of how to use the simple wrapper module.
'''

__author__ = "Shitalkumar Sawant"
__copyright__ = "Copyright(c) 2018 All rights reserved"

import time, sys

from cozmo.robot import Robot
import cozmo
from cozmo.lights import green_light, red_light, white_light, blue_light, off_light

from simple.wrapper import SimpleRobot


def movements(robot: Robot):
    simple = SimpleRobot(robot)

    simple.drive_forward_fast(30)
    simple.turn_right()
    simple.drive_backward(10)
    simple.drive_forward(20)
    simple.turn_left()
    simple.drive_forward_fast(20)


def go_to_cube(robot: Robot):
    simple = SimpleRobot(robot)
    simple.move_lift_low()
    simple.drive_to_cube()
    simple.move_lift_high()
    time.sleep(3)
    simple.move_lift_low()
    simple.drive_backward(10)


def lift_movements(robot: Robot):
    simple = SimpleRobot(robot)
    simple.say('Raising my lift')
    simple.move_lift_high()
    simple.say('Lift to mid position')
    simple.move_lift_mid()
    simple.say('Lowering my lift')
    simple.move_lift_low()


def head_movements(robot: Robot):
    simple = SimpleRobot(robot)
    simple.say("Move head high")
    simple.move_head_high()
    simple.say("Move head low")
    simple.move_head_low()
    simple.say("Move head straight")
    simple.move_head_straight()


def backpack_lights(robot: Robot):
    simple = SimpleRobot(robot)
    simple.set_backpack_lights(red_light, green_light, white_light, blue_light, red_light)
    time.sleep(5)
    simple.set_backpack_lights_off()
    simple.set_all_backpack_lights(red_light)
    time.sleep(3)
    simple.set_backpack_lights_off()


def cube_lights(robot: Robot):
    simple = SimpleRobot(robot)
    simple.set_cube_lights(1, blue_light.flash(off_color=cozmo.lights.white))
    simple.set_all_backpack_lights(blue_light)
    time.sleep(2)
    simple.set_cube_lights(2, green_light.flash(off_color=cozmo.lights.white))
    simple.set_all_backpack_lights(green_light)
    time.sleep(2)
    simple.set_cube_lights(3, red_light.flash(off_color=cozmo.lights.white))
    simple.set_all_backpack_lights(red_light.flash(off_color=cozmo.lights.white))
    time.sleep(2)
    time.sleep(4)
    simple.set_cube_lights_off(1)
    simple.set_cube_lights_off(2)
    simple.set_cube_lights_off(3)
    simple.set_backpack_lights_off()


def _when_cube_tapped(simple: SimpleRobot, cube):
    simple.set_cube_lights(cube, blue_light.flash(off_color=cozmo.lights.green))
    time.sleep(1)
    simple.set_cube_lights_off(cube)


def cube_tapped(robot: Robot):
    simple = SimpleRobot(robot)
    simple.when_cube_tapped(_when_cube_tapped, 1)
    simple.when_cube_tapped(_when_cube_tapped, 2)
    simple.when_cube_tapped(_when_cube_tapped, 3)
    simple.say("Tap a cube")
    time.sleep(10)


def actions(robot: Robot):
    simple = SimpleRobot(robot)
    simple.sleep()
    simple.act_bored()
    simple.act_like_dog()


def go_in_square(robot: Robot):
    simple = SimpleRobot(robot)
    for i in [1,2,3,4]:
        simple.drive_forward_fast(20)
        simple.turn_right()


def go_in_circle(robot: Robot):
    simple = SimpleRobot(robot)
    for _ in range(20):
        simple.drive_forward_fast(4, should_play_anim=False)
        simple.turn_right(degree=18)


'''
when cube 1 is tapped the counter is incremented.
when cube 2 is tapped the current count is announced
when cube 3 is tapped the program ends
'''
def counter_using_cubes(robot: Robot):
    simple = SimpleRobot(robot)
    exit_loop = False
    counter=0

    while not exit_loop:
        if simple.was_cube_tapped(1):
            simple.set_cube_lights(1, blue_light.flash(off_color=cozmo.lights.white))
            time.sleep(0.3)
            simple.set_cube_lights(1, off_light)
            counter += 1

            if counter >= 10:
                counter = 0
            print(counter)

        if simple.was_cube_tapped(2):
            simple.set_cube_lights(2, blue_light.flash(off_color=cozmo.lights.white))
            simple.say(str(counter))
            simple.set_cube_lights(2, off_light)

        if simple.was_cube_tapped(3):
            simple.set_cube_lights(3, red_light.flash(off_color=cozmo.lights.white))
            simple.say("Cube three tapped, bye!")
            simple.set_cube_lights(3, off_light)
            exit_loop = True

        time.sleep(0.3)


"""
Call the function that you want demoed.
"""
cozmo.run_program(lift_movements)

