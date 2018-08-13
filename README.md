# simple-cozmo

Implements a wrapper on the Anki Cozmo's python SDK. This wrapper makes it possible for younger students to program Cozmo in Python using a simple procedural style.

Anki Conzmo is a great platform for young children to begin learning programming. In United States they start learning Scratch based programming starting grade two. Cozmo code-lab offers user experience similar to the scratch block based programming style. At this age, however, it is difficult to pick up advanced programming concepts like OOP and event driven asynch programming. The Cozmo python SDK requires those skills.

Children already love playing with Cozmo. They easily gain familiarity with code-lab. Simple-cozmo is an attempt to bridge the gap of difficulty between code lab and the SDK. That motivates the children to graduate to using a real world programming language. 

# Using simple-cozmo

Quickest way to get started using simple-cozmo is to use an IDE like pycharm. Select requirements.txt in PyCharm (community edition) and let it download the required SDK version. You can then clone the github repository and start editing my-cozmo.py. 

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

In the above example, Cozmo prepares to lift a cube by lowering his lift. Then he looks around for a cube and drives to one, once found. Lifting the lift again, lifts the cube. Cozmo holds it for 3 seonds before placing it down and then moving back. As you can see, this program reduces the code by not having to write, code to setup cozmo, waiting for completion of action. It reduces number of parameters required to pass in to each function. The function names themselves are based on block names in the code-block application. Furthermore, since all the functions are accessible in SimpleCozmo, a python IDE's auto-completion makes it easy for younder kids to discover new functions and to type them fast.

You can find more examples in: demo-simple-cozmo.py. 

# Future

This is an initial version of simple-cozmo. Eventually it will be published as a module so that it is easy to install it using pip. For now I hope you do not mind implementing your code right within the cloned repository. This approach has been used successfully to teach python to 2nd, 3rd and 4th graders during summer.

Simple-cozmo already has all the functionality of code lab, with some exceptions (functions to draw on Cozmo's screen are missing). There is a plan to add this functionality and to implement some complete example games. 

Your feedback is welcome.  I do plan to enhance it per your input.
