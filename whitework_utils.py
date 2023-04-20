import turtlethread
from math import sin, cos, pi, tan, radians


def create_zigzag_unit_square(density, transposed):
    x = [0]
    y = [0]

    # Move forwards
    for p in range(1, density + 1):
        x.append(p % 2)
        y.append(p / density)

    x.append(0)
    y.append(1)

    # Move backwards
    for p in range(1, density + 1):
        x.append(p % 2)
        y.append(1 - p / density)

    x.append(0)
    y.append(0)

    if transposed:
        return y, x
    return x, y


def rotate(x, y, rotation):
    rot = radians(rotation)
    new_x = x * cos(rot) - y * sin(rot)
    new_y = x * sin(rot) + y * cos(rot)

    return new_x, new_y


def draw_zigzag_parallelogram(turtle, num_points, scale, direction, transposed):
    x0, y0 = turtle.position()
    rotation = turtle.angle

    x, y = create_zigzag_unit_square(num_points, transposed=transposed)
    for xi, yi in zip(x, y):
        xi += yi
        yi *= direction
        xi, yi = rotate(xi, yi, rotation)
        turtle.goto(x0 + scale * xi, y0 + scale * yi)


def draw_parallelogram(turtle, scale, mirror):
    with turtle.running_stitch(20):
        draw_zigzag_parallelogram(turtle, 3, scale, mirror, transposed=False)
        draw_zigzag_parallelogram(turtle, 3, scale, mirror, transposed=True)

    with turtle.running_stitch(scale * 10):  # No intermediate stitches
        draw_zigzag_parallelogram(turtle, 21, scale, mirror, transposed=False)


if __name__ == "__main__":
    needle = turtlethread.Turtle()
    print(needle.position())

    draw_rose(needle, scale=100, offset=20)

    needle.show_info()
    needle.save("rose_clean.png")
