"""
This class is a wrapper over Cozmo SDK. It allows a simpler procedural approach of programming Cozmo for younger
children.
"""

__all__ = ["SimpleRobot"]
__author__ = "Shitalkumar Sawant"
__copyright__ = "Copyright(c) 2018 All rights reserved"

from cozmo.robot import Robot
from cozmo.util import degrees, distance_mm, speed_mmps
import cozmo
from cozmo.lights import green_light, red_light, white_light, blue_light, off_light
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id, EvtObjectTapped

from .cubes import LightCubesEventsSerializer

DISTANCE_PER_STEP = distance_mm(10)
SPEED_NORMAL = speed_mmps(50)
SPEED_FAST = speed_mmps(100)


class SimpleRobot:
    #cube1 looks like a paperclip
    #cube2 looks like a lamp / heart
    #cube3 looks like the letters 'ab' over 'T'
    cube_Ids = [LightCube1Id, LightCube2Id, LightCube3Id]

    def _get_cube(self, cube_no=1):
        return self.robot.world.get_light_cube(self.cube_Ids[cube_no-1])

    def __init__(self, robot: Robot):
        self.robot = robot
        self.cubeEventsSerializer = LightCubesEventsSerializer(self.robot)

    def drive_forward(self, steps):
        self.robot.drive_straight(DISTANCE_PER_STEP * steps, SPEED_NORMAL).wait_for_completed()

    def drive_backward(self, steps):
        self.robot.drive_straight(DISTANCE_PER_STEP * -steps, SPEED_NORMAL).wait_for_completed()

    def drive_forward_fast(self, steps, should_play_anim=True,wait_for_completed=True):
        action = self.robot.drive_straight(DISTANCE_PER_STEP * steps, SPEED_FAST,
                                           should_play_anim=should_play_anim, in_parallel=not wait_for_completed)
        if wait_for_completed:
            action.wait_for_completed()
            return None
        return action

    def drive_backward_fast(self, steps):
        self.robot.drive_straight(DISTANCE_PER_STEP * -steps, SPEED_FAST).wait_for_completed()

    def turn_right(self, degree=90, wait_for_completed=True):
        action = self.robot.turn_in_place(degrees(-degree), in_parallel=not wait_for_completed)
        if wait_for_completed:
            action.wait_for_completed()
            return None
        return action

    def turn_left(self, degree=90):
        self.robot.turn_in_place(degrees(degree)).wait_for_completed()

    def drive_to_cube(self):
        robot = self.robot

        robot.set_head_angle(degrees(-5.0)).wait_for_completed()

        print("Cozmo is waiting until he sees a cube.")
        cube = robot.world.wait_for_observed_light_cube()

        print("Cozmo found a cube, and will now attempt to dock with it:")
        action = robot.dock_with_cube(cube, num_retries=2)
        action.wait_for_completed()
        print("result:", action.result)

    def move_lift_low(self):
        self.robot.set_lift_height(0).wait_for_completed()

    def move_lift_mid(self):
        self.robot.set_lift_height(0.5).wait_for_completed()

    def move_lift_high(self):
        self.robot.set_lift_height(1).wait_for_completed()

    def move_lift(self, height):
        self.robot.set_lift_height(height).wait_for_completed()

    def move_head_low(self):
        self.robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()

    def move_head_straight(self):
        self.robot.set_head_angle(degrees(0)).wait_for_completed()

    def move_head_high(self):
        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    def say(self, text):
        self.robot.say_text(text).wait_for_completed()

    def set_backpack_lights(self, light1, light2, light3, light4, light5):
        self.robot.set_backpack_lights(light1, light2, light3, light4, light5)

    def set_all_backpack_lights(self, light):
        self.robot.set_all_backpack_lights(light)

    def set_backpack_lights_off(self):
        self.robot.set_backpack_lights_off()

    def set_cube_lights(self, cube_no=1, color=blue_light):
        cube = self._get_cube(cube_no)

        if cube is None:
            cozmo.logger.warning("Cozmo is not connected to a "+cube_no+" check the battery.")
        else:
            cube.set_lights(color)

    def set_cube_lights_off(self, cube_no=1):
        cube = self._get_cube(cube_no)

        if cube is None:
            cozmo.logger.warning("Cozmo is not connected to a "+cube_no+" check the battery.")
        else:
            cube.set_lights_off()

    def when_cube_tapped (self, f, cube_no=None):
        cube = self._get_cube(cube_no)

        def cube_tapped_handler(evt, obj=None, tap_count=None, **kwargs):
            f(self, cube_no)

        if cube is None:
            cozmo.logger.warning("Cozmo is not connected to a " + cube_no + " check the battery.")
        else:
            cube.add_event_handler(EvtObjectTapped, cube_tapped_handler)

    def was_cube_tapped(self, cube_no) -> bool:
        return self.cubeEventsSerializer.was_cube_tapped(cube_no)

    def play_trigger (self, trigger_name):
        self.robot.play_anim_trigger(getattr(cozmo.anim.Triggers, trigger_name)).wait_for_completed()

    def act_happy(self):
        self.play_trigger("CodeLabHappy")

    def act_like_winner(self):
        self.play_trigger("CodeLabWin")

    def act_sad(self):
        self.play_trigger("CodeLabUnhappy")

    def act_surprised(self):
        self.play_trigger("CodeLabSurprise")

    def act_like_dog(self):
        self.play_trigger("CodeLabDog")

    def act_like_cat(self):
        self.play_trigger("CodeLabCat")

    def sneeze(self):
        self.play_trigger("CodeLabSneeze")

    def act_excited(self):
        self.play_trigger("CodeLabExcited")

    def think_hard(self):
        self.play_trigger("CodeLabThinking")

    def act_bored(self):
        self.play_trigger("CodeLabBored")

    def act_frustrated(self):
        self.play_trigger("CodeLabFrustrated")

    def act_chatty(self):
        self.play_trigger("CodeLabChatty")

    def act_disappointed(self):
        self.play_trigger("CodeLabDejected")

    def sleep(self):
        self.play_trigger("CodeLabSleep")

'''    
    
    set_cube_light_effect (cube_no, spin/blink, color)
    
    when_cube_tapped(cube=any/1,2,3)
    when_cube_moved(cube=any/1,2,3)
    when_cube_seen (cube=any/1,2,3)
    
    draw_text_at_xy (text, x,y) 
    set_text_scale_to (percentage)
    set_text_alignment_to (top, left)
    
    draw_line
    draw_rectangle
    fill_rectangle
    draw_circle
    fill_circle
    
    mystery_animation
    wait_to_see_face
    wait__to_see_smile
    wait_to_see_frown
    wait_to_see_cube
    wait_for_cube_tap
    
'''
