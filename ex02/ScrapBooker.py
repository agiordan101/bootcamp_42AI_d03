from matplotlib import image
import numpy as np


class ScrapBooker:

    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        shape = np.shape(array)
        if (position[0] < 0 or shape[0] < position[0] + dimensions[0]
           or position[1] < 0 or shape[1] < position[1] + dimensions[1]):
            print("Dimensions or position is wrong")
            return
        array_crop = []
        for i in range(dimensions[0]):
            array_crop.append(array[position[0] + i]
                              [position[1]:position[1] + dimensions[1]])
        return array_crop

    def thin(self, array, n, axis):
        size = np.shape(array)
        if n == 0:
            return None
        i = 1
        if axis:
            while i * n < size[0]:
                array = np.delete(array, i * n - 1, 1)
                i += 1
        else:
            while i * n < size[1]:
                array = np.delete(array, i * n - 1, 0)
                i += 1
        return array

    def juxtapose(self, array, n, axis):
        array_jux = array
        for i in range(1, n):
            array_jux = np.concatenate((array_jux, array), axis)
        return array_jux

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)


array = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
sb = ScrapBooker()
print(sb.crop(array, (2, 2), (1, 1)))
print()

print(sb.thin(array, 2, 1))
print(sb.thin(array, 2, 0))
print()

print(sb.juxtapose(array, 2, 1))
print(sb.juxtapose(array, 2, 0))
print()

print(sb.mosaic(array, (2, 2)))
