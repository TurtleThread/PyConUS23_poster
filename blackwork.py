import turtlethread

# The following imports are available on GitHub
from blackwork_utils import (
    draw_cross_line,
    draw_staircase,
    draw_flower
)


def draw_column(pen, unit, d, length):
    for n in range(length):
        # Draw a flower after iteration 1
        if n > 0:
            pen.forward(unit*2)
            draw_flower(pen, unit, d)
            pen.forward(unit*2)
        
        # Mirror symmetry
        for m in [1, -1]:
            direction = d*m
            
            # Straight line
            pen.forward(12*unit)
            pen.left(-90*direction)
            pen.forward(unit)
            pen.left(-90*direction)
            
            # Staircase and crosses
            draw_cross_line(
                pen, unit, direction
            )
            draw_staircase(
                pen, unit, direction
            )
            draw_cross_line(
                pen, unit, -direction
            )
            
            # Straight line
            pen.left(90*direction)
            pen.forward(unit)
            pen.left(90*direction)
            pen.forward(12*unit)
            
            # Flower separator
            if m == 1:
                pen.forward(unit*2)
                draw_flower(pen, unit, -direction)
                pen.forward(unit*2)
        
unit = 12

pen = turtlethread.Turtle()
pen.left(-90)
for offset in range(4):
    if offset > 0:
        with pen.jump_stitch():
            pen.goto(0 + 2 * offset * 14 * unit, 0)
    
    # Draw left column
    with pen.running_stitch(unit):
        draw_column(pen, unit, 1, 5)
    
    # Move to top
    with pen.jump_stitch():
        pen.goto(unit + 2 * offset * 14 * unit, 0)
    
    # Draw right column
    with pen.running_stitch(unit):
        draw_column(pen, unit, -1, 5)

pen.save("blackwork.png")