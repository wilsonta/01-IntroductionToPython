"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Tim Wilson.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
redturtle = rg.SimpleTurtle('turtle')
redturtle.pen = rg.Pen('red', 5)
redturtle.speed = 10

size = 200

for k in range(6):
    redturtle.draw_square(size)

    redturtle.pen_up()
    redturtle.right(90)
    redturtle.forward(15)
    redturtle.left(30+k)

    redturtle.pen_down()
    size = size - 30

greenturtle=rg.SimpleTurtle('turtle')
greenturtle=rg.Pen('green',3)
greenturtle.speed=20

size=200

for k in range(20):

    greenturtle.left(45)
    greenturtle.forward(20)


    greenturtle.pen_up()
    greenturtle.left(45+k)
    greenturtle.forward(5)

    greenturtle.pen_down()
    size=size-50
window.close_on_mouse_click()

