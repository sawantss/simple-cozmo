# simple-cozmo

Implements a wrapper on the Anki Cozmo's python SDK. This wrapper makes it possible for younger students to program Cozmo in Python using a simple procedural style.

Anki Conzmo is a great platform for young children to begin learning programming. In United States they start learning Scratch based programming starting grade two. Cozmo code-lab offers user experience similar to the scratch block based programming style. At this age, however, it is difficult to pick up advanced programming concepts like OOP and event driven programming.  The Cozmo python SDK requires those skills.

Children already love playing with Cozmo. They easily gain familiarity with code-lab. Simple-cozmo is an attempt to bridge the gap of difficulty between code lab and the SDK. That motivates the children to graduate to using a real world programming language. 

# Using simple-cozmo

Quickest way to get started using simple-cozmo is to use an IDE like pycharm. Select requirements.txt in MyCharm and let it download the required SDK version. You can then clone the github repository and start editing my-cozmo.py. 

A sample program using simple-cozmo is given below:

```python

import time
from cozmo.robot import Robot
from simple.wrapper import SimpleRobot

def move_a_cube(robot: Robot):
    simple = SimpleRobot(robot)
    simple.move_lift_low()
    simple.drive_to_cube()
    simple.move_lift_high()
    time.sleep(3)
    simple.move_lift_low()
    simple.drive_backward(10)

cozmo.run_program(move_a_cube)
```

You can find more examples in: demo-simple-cozmo.py. 

# Future

This is an initial version of simple-cozmo. I plan to publish it as a module so that it will be easy to install it using pip. For now I hope you do not mind implementing your code right within the cloned repository. This approach has been used successfully to team python to 2nd, 3rd and 4th graders during summar.

Simple-cozmo already has all the functionality of code lab, with some exceptions (functions to draw on Cozmo's screen are missing). I plan to add this functionality and to implement some complete example games. 

Your feedback is welcome.  I do plan to enhance it per your input.
