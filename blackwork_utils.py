import turtlethread


def left_and_forward(needle, angle, unit):
    needle.left(angle)
    needle.forward(unit)


def draw_flower_head(needle, unit, direction=1):
    needle.forward(unit)

    parameters = (  # Angle, length
        (90, 1),
        (90, 3),
        (-90, 1),
        (-90, 1),
        (90, 1),
        (-90, 1.5),
        (-90, 1),
        (90, 0.5),
        (90, 0.5),
        (90, 1),
        (-90, 1.5),
        (-90, 1),
        (90, 1),
        (-90, 1),
    )

    for i in range(4):
        needle.forward(unit * 3)

        for angle, l in parameters:
            left_and_forward(needle, angle * direction, l * unit)

        needle.left(-90 * direction)

    left_and_forward(needle, 90 * direction, unit)
    left_and_forward(needle, 90 * direction, unit)


def draw_top_hat(needle, unit, direction=1):
    needle.forward(unit)

    left_and_forward(needle, 90 * direction, unit)
    left_and_forward(needle, -90 * direction, unit)
    left_and_forward(needle, -90 * direction, unit)
    left_and_forward(needle, 90 * direction, unit)


def draw_half_cross(needle, unit, direction=1):
    draw_top_hat(needle, unit=unit, direction=direction)
    needle.forward(unit)
    needle.left(direction * 90)
    needle.forward(unit)
    draw_top_hat(needle, unit=unit, direction=direction)


def draw_cross_line(needle, unit, direction):
    draw_half_cross(needle, unit, direction)
    needle.left(-90 * direction)
    needle.forward(unit)
    needle.left(-90 * direction)
    draw_half_cross(needle, unit, direction)


def draw_staircase(needle, unit, direction):
    needle.forward(2 * unit)

    needle.left(90 * direction)
    for i in range(10):
        needle.forward(unit)
        needle.left(90 * direction)
        needle.forward(unit)
        needle.left(-90 * direction)

    needle.forward(unit)
    needle.left(-90 * direction)

    needle.forward(2 * unit)


def draw_flower(needle, unit, direction):
    needle.left(-90 * direction)
    needle.forward(unit)
    needle.left(90 * direction)
    needle.forward(unit)

    needle.left(-90 * direction)
    draw_flower_head(needle, unit, direction)
    needle.left(-90 * direction)

    needle.forward(unit)
    needle.left(90 * direction)
    needle.forward(unit)
    needle.left(-90 * direction)
