import turtlethread
from math import pi, sin, cos

def draw_rose(pen, n, d, r0):
    x0, y0 = pen.position()
    for theta in range(0, 361, 1):
        k = theta * d * pi / 180
        r = r0 * sin(n * k)
        x = r * cos(k)
        y = r * sin(k)
        needle.goto(x0 + x, y0 + y)

needle = turtlethread.Turtle()

# Draw first rose
with needle.running_stitch(50):
    draw_rose(needle, 5, 97, 570)
    
# Move a bit more than two radii
with needle.jump_stitch():
    needle.forward(1150)

# Draw second rose
with needle.running_stitch(50):
    draw_rose(needle, 6, 71, 570)
    
needle.save("maurer_rose.jef")