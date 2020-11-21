from math import sqrt, pi, sin, cos

unit = 1  # refers to the unit length of each individual arrow - this is tbd
height = 100  # refers to the y coordinate for the source and detector points (which will be directly opposite each
# other


# height will just be a set constant
# point_x is the point where the light beam reflects off teh horizontal surface
# source_x and detector_x are the x coordinates of the source and detector points
# source_x I expect will be negative (on the left hand side of the origin) and detector_x positive, but this is tbd
def individual_arrows(frequency, source_x, detector_x, point_x):
    period = (1 / frequency)
    speed_light = 3.8e8
    distance = sqrt((height ** 2) + ((source_x - point_x) ** 2)) + sqrt((height ** 2) + ((point_x - detector_x) ** 2))
    # using pythagoras' theorem to find the distance the light travels before and after it has been reflected
    time = distance / speed_light
    rotation = (time / period) - ((time / period) // 1)  # this gives the final turn of the arrow
    angle = 2 * pi * rotation  # might change the 2pi for 360 degrees - actually sin() uses rads
    x = unit * sin(angle)  # x and y are the change in x and y coordinates when the unit line is rotated
    y = unit * cos(angle)
    # after this you would need to create a line from xorigin, yorigin (this point is tbd) and xorigin+x,yorigin+y
    # additionally final arrow uses the origin points iteratively so the placement of these variables is key
