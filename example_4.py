import turtlethread
from random import gauss
from example_2 import draw_square

def random_flower(needle, length, noise):    
    for petal in range(8):
        # Choose petal size and angle
        l = gauss(length, noise*length)
        a = gauss(45, noise*45)
        
        draw_square(needle, l)
        needle.right(a)

needle = turtlethread.Turtle()
for x in range(0, 1951, 150):
    # Set noise level
    n = 0.4 * (x / 1950)**1.4
    for y in range(0, 751, 150):
        # Choose random offset and rotation
        dx = gauss(0, 50*n)
        dy = gauss(0, 50*n)
        da = gauss(0, 90*n)
        
        # Move to random offset
        with needle.jump_stitch():
            needle.goto(x + dx, y + dy)
            needle.setheading(da)
        
        # Embroider random flower
        with needle.running_stitch(25):
            random_flower(needle, 50, n)

needle.save("field_schotter.png")