import math
import numpy as np
from math import sqrt, pi, sin, cos
import matplotlib.pyplot as plt

#   VARIABLES

wavelength = float(input("wavelength in nm"))
angstrom_wavelength = wavelength * 10  # converts wavelength from nm to angstroms
height = 100  # the set value for the y coordinate of the source and detector (they are directly opposite each other)
constant_source_x = -50  # the set value for the x coordinate of the source
constant_detector_x = 50  # the set value for the x coordinate of the detector
constant_point_x = list()  # constant_point_x holds the list which will come from the database holding all the
# point_x values that correspond to the users n value input
unit = 1  # this is length of all the individual arrows - this could be subject to change
test_nvalues_db = [-450 / 11, -350 / 11, -250 / 11, -150 / 11, -50 / 11, 50 / 11, 150 / 11, 250 / 11, 350 / 11,
                   450 / 11]  # this is test data for n=10, Sx=-50, Dx=50
input_frequency = 3.8 * 10e8 / (wavelength * 10e-9)  # 10e-9 to convert to m
n = int(10)  # this is test data
list_ind = list()  # list_ind used to store x y coordinates of individual_arrow function output


#   FUNCTIONS

# this is a guassian function, which is then used in the functions for X,Y and Z
# parameters:
# w=wavelength of the light source, from the user input
# alpha, mu, s1 and s2 are just constants dictated in the x, y or z _funcs
# output:
# the value that wavelength takes on the guassian distribution
def gauss(w, alpha, mu, sigma_1, sigma_2):
    if w < mu:  # the value of sigma used (s1 or s2) is determined by whether the wavelength is smaller than...
        sigma = sigma_1  # than the value of mu
    else:
        sigma = sigma_2
    top = pow(w - mu, 2)  # TODO: replace all pows with ** or vv
    bottom = -2 * pow(sigma, 2)
    g_product = alpha * (math.exp(top / bottom))
    return g_product


# parameter: w=wavelength
# output: the X, Y or Z value (respectively) of the wavelength's coordinate on the CIE colour space
def x_func(w):
    x_val = gauss(w, 1.056, 5998, 379, 310) + gauss(w, 0.362, 4420, 160, 267) + gauss(w, -0.065, 5011, 204, 262)
    return x_val


def y_func(w):
    y_val = gauss(w, 0.821, 5688, 469, 405) + gauss(w, 0.286, 5309, 163, 311)
    return y_val


def z_func(w):
    z_val = gauss(w, 1.217, 4370, 118, 360) + gauss(w, 0.681, 590, 260, 138)
    return z_val


# the functions below (gamma_correct and clip_range) are used for the function xyz_to_rgb
def gamma_correct(u):  # these make the value u a gamma compressed value, u is (r/g/b)_linear
    if u <= 0.031308:
        g_compressed = (12.92 * u)
    else:
        g_compressed = (1.055 * (u ** (1 / 2.4))) - 0.055
    return g_compressed


def clip_range(value_to_clip):  # this function removes invalid values of RGB, value_to_clip is gamma_correct(u)
    if not 0 <= value_to_clip <= 1:
        if value_to_clip < 0:
            value_to_clip = 0
        else:
            value_to_clip = 1
    return value_to_clip


# xyz_to_rgb
# parameters: wavelength in angstroms
# output: the rgb code that corresponds to the wavelength
def xyz_to_rgb(w):
    matrix1 = np.array([[3.24096994, -1.53738318, -0.49861076], [-0.96924364, 1.8759675, 0.04155506],
                        [0.05563008, -0.20397696, 1.05697151]])
    xyz_matrix = np.array([x_func(w), y_func(w), z_func(w)])
    rgb_matrix = matrix1.dot(xyz_matrix)
    r_linear = (rgb_matrix[0])
    g_linear = (rgb_matrix[1])
    b_linear = (rgb_matrix[2])
    r = 255 * clip_range(gamma_correct(r_linear))
    g = 255 * clip_range(gamma_correct(g_linear))
    b = 255 * clip_range(gamma_correct(b_linear))
    if r >= g and r >= b:
        difference = 255 - r
        r = 255
        g = g + difference
        b = b + difference
    elif g >= r and g >= b:
        difference = 255 - g
        r = r + difference
        g = 255
        b = b + difference
    else:
        difference = 255 - b
        r = r + difference
        g = g + difference
        b = 255
    return r, g, b  # I am not sure how I am going to return the rgb values so this is just a placeholder


# parameters: frequency (called input_frequency in outer scope) point_x (constant_point_x)is the point where the
# light beam reflects off the horizontal surface (dependent on the value of n input) source_x (constant_source_x in
# outer scope) and detector_x (constant_detector_x in outer scope) are the x coordinates of the source and detector
# points source_x I expect will be negative (on the left hand side of the origin) and detector_x positive, but this is
# tbd output: the x and y coordinate for the rotated line
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


# parameters: x and y (the output from individual_arrow)
# output: the data for a matplotlib graph using the s and y coordinates
def graph_ind_arrow(x, y, ):
    plt.plot([0, x], [0, y], color=(red, green,
                                    blue))  # creates a graph that plots a line from 0,0 to x,y using the r g and b
    # values
    # from the frequency_to_rgb procedure
    # this will need to be expanded and refined when I start creating the UI
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)  # these set the axis range to -1 to 1 in both the x and y direction
    plt.tick_params(axis='x', which='both', bottom=False, top=False,
                    labelbottom=False)  # taken from pythonmatplotlibtips.blogspot.com, see references for link
    plt.tick_params(axis='y', which='both', right=False, left=False,
                    labelleft=False)  # removes axis labels, lines and ticks
    for pos1 in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos1].set_visible(False)


#   END OF FUNCTIONS

red = (
          xyz_to_rgb(angstrom_wavelength)[
              0]) / 255  # converts the rgb value from xyz_to_rgb() to a decimal between 0 and 1
green = (xyz_to_rgb(angstrom_wavelength)[1]) / 255
blue = (xyz_to_rgb(angstrom_wavelength)[2]) / 255
for count in range(0, n):  # 0 up to n-1, iterates through all values of point_x
    constant_point_x = test_nvalues_db[
        count]  # test_nvalues_db will be replaced with the list produced by the database when the database section
    # is complete
    temp_x = individual_arrows(input_frequency, constant_source_x, constant_detector_x, constant_point_x)[
        0]  # takes the x value output from individual_arrows
    temp_y = individual_arrows(input_frequency, constant_source_x, constant_detector_x, constant_point_x)[
        1]  # takes the y value
    graph_ind_arrow(temp_x, temp_y)
    plt.savefig(str(count) + '.png')  # save the figure produced in graph_ind_arrow to a png
    plt.clf()  # clear the figure for the next iteration
    ind_out = (
        individual_arrows(input_frequency, constant_source_x, constant_detector_x, constant_point_x))  # ind_out=the
    # list of the x and y coordinate
    list_ind.append(ind_out)

# below is the subsection finalArrow - this is not in a function as this is only run once - but this is tbd
list_x = list()  # holds all x coordinate values from ind_out
list_y = list()  # holds all y coordinate values from ind_out
list_x.append(list_ind[0][0])
list_y.append(list_ind[0][1])
for count_n in range(1, n):  # this starts from 0 to n-1 (the first arrow is found at [0][0] and [0][1])
    list_x.append(list_ind[count_n][0] + (list_x[count_n - 1]))  # these lists have been formatted for final arrow
    list_y.append(list_ind[count_n][1] + list_y[(
                                                    count_n) - 1])  # each value is their original value from
    # list_ind plus all of the corresponding values summed before it

plt.plot(list_x, list_y, color=(
    red, green, blue))  # plot x coordinates and y coordinates using the corresponding colour for the frequency inputted
plt.plot([list_x[0], list_x[n - 1]], [list_y[0], list_y[n - 1]],
         color=(0, 0, 0))  # plot a line that connects first point to last point in black
plt.tick_params(axis='x', which='both', bottom=False, top=False,
                labelbottom=False)  # taken from pythonmatplotlibtips.blogspot.com, see references for link
plt.tick_params(axis='y', which='both', right=False, left=False,
                labelleft=False)  # removes axis labels, lines and ticks
for pos in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.savefig('finalArrow.png')  # save the figure
plt.clf()  # clear the figure
