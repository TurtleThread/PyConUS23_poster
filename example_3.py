import turtlethread
from example_2 import draw_square

def draw_flower(needle, length):
    for petal in range(8):
        draw_square(needle, length)
        needle.right(45)

needle = turtlethread.Turtle()
with needle.running_stitch(20):
    draw_flower(needle, 230)

needle.save("flower.jef")