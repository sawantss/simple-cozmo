"""
This class makes it easier to deal with cube tapped events in a procedural way using if statements.
"""

from __future__ import with_statement

__all__ = ["LightCubesEventsSerializer"]
__author__ = "Shitalkumar Sawant"
__copyright__ = "Copyright(c) 2018 All rights reserved"

from threading import Lock

import cozmo
from cozmo.robot import Robot
from cozmo.objects import LightCube, LightCube1Id, LightCube2Id, LightCube3Id, EvtObjectTapped


class LightCubesEventsSerializer:
    cube_Ids = [LightCube1Id, LightCube2Id, LightCube3Id]
    taps_status_locks = [Lock(), Lock(), Lock()]
    taps_status = [False, False, False]

    def __init__(self, robot: Robot):
        self.robot = robot

        for i in range(1, 4):
            self.when_cube_tapped(self._cube_tapped, i)

    def _cube_tapped(self, cube_no):
        print("Cube tapped: ", cube_no)
        with self.taps_status_locks[cube_no - 1]:
            self.taps_status[cube_no - 1] = True

    def _get_cube(self, cube_no=1) -> LightCube:
        return self.robot.world.get_light_cube(self.cube_Ids[cube_no-1])

    def when_cube_tapped (self, f, cube_no=None):
        cube = self._get_cube(cube_no)

        def cube_tapped_handler(evt, obj=None, tap_count=None, **kwargs):
            f(cube_no)

        if cube is None:
            cozmo.logger.warning("Cozmo is not connected to a " + cube_no + " check the battery.")
        else:
            cube.add_event_handler(EvtObjectTapped, cube_tapped_handler)

    """
    Returns true if the specified cube was tapped since this method was called last
    
    cube_no must be an integer in the range of 1 to 3
    """
    def was_cube_tapped(self, cube_no) -> bool:
        cube_tapped = False

        with self.taps_status_locks[cube_no - 1]:
            if self.taps_status[cube_no - 1] > 0:
                cube_tapped=True
            self.taps_status[cube_no - 1] = False

        return cube_tapped
