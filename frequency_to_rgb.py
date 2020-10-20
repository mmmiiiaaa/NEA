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
    top = pow(w - mu, 2) # TODO: replace all pows with ** or vv
    bottom = -2 * pow(sigma, 2)
    g_product = alpha * (math.exp(top/bottom))

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
        g_compressed=(12.92 * u)
    else:
        g_compressed=(1.055 * (u ** (1 / 2.4))) - 0.055
    return g_compressed



def clip_range(value_to_clip):  # this function removes invalid values of RGB
    if not 0 <= value_to_clip <= 1:
        if value_to_clip < 0:
            value_to_clip = 0
        else:
            value_to_clip = 1
    return value_to_clip


# xyz_to_rgb
# parameters: wavelength
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
    return (r, g, b)  # I am not sure how I am going to return the rgb values so this is just a placeholder


#code below is just used to test inputs and outputs

w = float(input("input wavelength in nm"))
w = w * 10  # multiply by 10 because functions use wavelength in angstroms (0.1 of a nm)
print(xyz_to_rgb(w))

#below is part of the code from the function xyz_to_rgb

# matrix1 = np.array([[3.24096994, -1.53738318, -0.49861076], [-0.96924364, 1.8759675, 0.04155506],
#                         [0.05563008, -0.20397696, 1.05697151]])
# xyz_matrix = np.array([x_func(w), y_func(w), z_func(w)])
# rgb_matrix = matrix1.dot(xyz_matrix)
# r_linear = (rgb_matrix[0])
# g_linear = (rgb_matrix[1])
# b_linear = (rgb_matrix[2])
# r = 255 * clip_range(gamma_correct(r_linear))
# g = 255 * clip_range(gamma_correct(g_linear))
# b = 255 * clip_range(gamma_correct(b_linear))
#
# print("next line of values are the values of r g b before they get incremented (so that at least one equals 255")
# print (r, g, b)
#
# print("next 3 lines of values are the values of r_linear, g_linear, and b_linear")
# print(r_linear)
# print(g_linear)
# print(b_linear)
#
# print("next 2 lines of values are the values of X Y and Z from the functions for the CIE colour space")
# print(x_func(w))
# print(y_func(w))
# print(z_func(w))
#
# print("next line prints the first value used in the x_func")
# print(gauss(w, 1.056, 5998, 379, 310))
# alpha=1.056
# mu=5998
# sigma_1=379 # I have removed if statement for deciding sigma here as I am using 500nm as my test input and know that
# # for the first gausiian function sigma1 is used for 500nm
# top=pow(w - mu, 2)
# bottom=-2*pow(sigma_1, 2)
# print(np.exp(top/bottom))
