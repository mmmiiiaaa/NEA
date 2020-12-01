from math import sqrt, pi, sin, cos
import matplotlib.pyplot as plt

unit = 1  # refers to the unit length of each individual arrow - this is tbd
height = 100  # refers to the y coordinate for the source and detector points (which will be directly opposite)


# height will just be a set constant


# point_x is the point where the light beam reflects off the horizontal surface (dependent on the value of n input)
# source_x and detector_x are the x coordinates of the source and detector points
# source_x I expect will be negative (on the left hand side of the origin) and detector_x positive, but this is tbd
def individual_arrows(frequency, source_x, detector_x, point_x):
    period = (1 / frequency)  # WILL HAVE TO ENSURE WHEN THE FREQUENCY IS INPUT IT IS KEPT IN UNIT Hz
    speed_light = 3.8e8
    distance = sqrt((height ** 2) + ((source_x - point_x) ** 2)) + sqrt((height ** 2) + ((point_x - detector_x) ** 2))
    # using pythagoras' theorem to find the distance the light travels before and after it has been reflected
    time = distance / speed_light
    rotation = (time / period) - ((time / period) // 1)  # this gives the final turn of the arrow
    angle = 2 * pi * rotation
    x = unit * sin(angle)  # x and y are the change in x and y coordinates when the unit line is rotated
    y = unit * cos(angle)
    return x, y



def graph_ind_arrow(x, y, ):
    plt.plot([0, x], [0, y], color=(r, g,
                                    b))  # creates a graph that plots a line from 0,0 to x,y using the r g and b values
    # from the frequency_to_rgb procedure
    # this will need to be expanded and refined when I start creating the UI


# # __TEST AREA__
# r = (int(
#     input("input r"))) / 255  # formatplotlib rgb values should be from 0 to 1 so I will need to take the rgb values
# # and divide by 255
# g = (int(input("input g"))) / 255
# b = (int(input("input b"))) / 255
# source_x = int(input("input source_x"))
# detector_x = int(input("input detector_x"))
# point_x = int(input("input point_x"))
# frequency = float(input("input frequency"))
# individual_arrows(frequency, source_x, detector_x, point_x)
# # graph_ind_arrow(x,y)
# print(x, y)
individual_arrows(760000000000000, -50, 50, 0)
print(x,y)
