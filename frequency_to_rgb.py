import math
import numpy as np


# w may have to be changed to another name, as will have to refer to the wavelength variable used throughout program


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
    g_product = alpha * math.exp(((w - mu) ^ 2) / -2 * (sigma ^ 2))

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

def gamma_correct(u):  # these make the value u a gamma compressed value
    if u <= 0.031308:
        return 12.92 * u
    else:
        return (1.055 * (u ^ (1 / 2.4))) - 0.055


def clip_range(value_to_clip):  # this function removes invalid values of RGB
    if not 0 <= value_to_clip <= 1:
        if value_to_clip < 0:
            value_to_clip = 0
        else:
            value_to_clip = 1
    return value_to_clip

# xyz_to_rgb
#parameters: wavelength
#output: the rgb code that corresponds to the wavelength

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
    return (r, g, b)  # I am not sure how I am going to return the rgb values so this is just a placeholder


w=float(input("input wavelength in nm"))
w=w*0.1 # multiply by 0.1 because functions use wavelength in angstroms (0.1 of a nm)
print(xyz_to_rgb(w))