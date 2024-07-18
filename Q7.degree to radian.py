import math
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)
degrees = 15
radians = degrees_to_radians(degrees)
print(degrees," degrees = ",radians,"radians.")