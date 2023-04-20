import turtlethread

def draw_square(needle, length):
    for side in range(4):
        needle.forward(length)
        needle.right(90)

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    draw_square(needle, 400)

needle.save("square.jef")