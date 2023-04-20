import turtlethread

# The following import is available on GitHub
from whitework_utils import draw_parallelogram

# Border
def forward_and_left(pen, a, l):
    pen.forward(l)
    pen.left(a)
    
def step(pen, w, h, d):
    forward_and_left(pen, -d*90, w)
    forward_and_left(pen, d*90, h)
    forward_and_left(pen, d*90, w)
    forward_and_left(pen, -d*90, h)
    
def walk(pen, w, h, steps, d):
    for i in range(steps):
        step(pen, w, h, d)

def border(pen, w, h, steps, n_triangles, d):
    x0, y0 = pen.position()

    for row in range(steps):
        # Adjust row starting position
        with pen.jump_stitch():
            x = x0 + row*w
            y = y0 + d*row*h
            pen.goto(x, y)

        for tri in range(n_triangles):
            # Make row of border
            with pen.running_stitch(w):
                walk(pen, w, h, steps-row, d)
            
            # If we're not on final triangle
            if tri != n_triangles-1:
                with pen.jump_stitch():
                    pen.forward(w*2*row)
        
        # End row with a short line
        with pen.running_stitch(w):
            pen.forward(w)

# Rose
def rose(pen, offset, scale):
    x0, y0 = pen.position()
    for n in range(4):
        pen.right(90)
        for mirror in (1, -1):
            # Add offset to petals
            with pen.jump_stitch():
                pen.right(mirror*17)
                pen.forward(offset)
                pen.right(-mirror*17)
            
            # Draw a petal as a parallellogram
            draw_parallelogram(
                pen, scale, mirror
            )
            
            # Go back to center again
            with pen.jump_stitch():
                pen.right(mirror*17)
                pen.forward(-offset)
                pen.right(-mirror*17)

pen = turtlethread.Turtle()

# Border
for y, d in [[-750, 1], [750, -1]]: 
    pen.goto(-972, y)
    border(pen, 24, 18, 10, 4, d)

# Roses
for x in [-732, 0, 732]:
    pen.goto(x, 0)
    rose(pen, 20, 100)

pen.save("whitework.png")