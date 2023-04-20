import turtlethread

def hilbert(pen, length, n, angle=90):
    if n == 0:
        return

    pen.right(angle)
    hilbert(pen, length, n-1, -angle)
    pen.forward(length)
    
    pen.left(angle)
    hilbert(pen, length, n-1, angle)
    pen.forward(length)
    hilbert(pen, length, n-1, angle)
    pen.left(angle)
    
    pen.forward(length)
    hilbert(pen, length, n-1, -angle)
    pen.right(angle)


pen = turtlethread.Turtle()

# Draw first, low resolution, curve
with pen.running_stitch(2*18):
    hilbert(pen, 2*18, 5)
    
    # Add space
    pen.forward(18)

# Draw second, high resolution, curve
with pen.running_stitch(18):
    hilbert(pen, 18, 6)

pen.save("hilbert.jef")