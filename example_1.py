import turtlethread

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    needle.forward(400)

needle.save("line.jef")