import numpy as np
from matplotlib import image
from matplotlib import pyplot


class ColorFilter:

    def __init__(self):
        pass

    def invert(self, array):
        for line in array:
            for i in range(len(line)):
                line[i] = 1 - line[i]
        return array

    def to_blue(array):
        return array


cf = ColorFilter()

array = np.array(image.imread("../koala.png"))
print(array)
inv = cf.invert(array)
pyplot.imshow(inv)
pyplot.show()
