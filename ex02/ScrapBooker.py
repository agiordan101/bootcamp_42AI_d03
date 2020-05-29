from matplotlib import image
import numpy as np

class ScrapBooker:

    def __init__(self):
        pass
    
    def crop(self, array, dimensions, position=(0, 0)):
        print(dimensions + position)
        width = array.shape[1]
        height = array.shape[0]
        array_crop = []
        for i in range(position[0], position[0] + dimensions[0]):
            if i > height:
                print("Y dimension are is of image")
            for j in range(position[1], position[1] + dimensions[1]):
                if j > width:
                    print("X dimension is out of image")
                array_crop.append(array[i * width + j])
        return np.array(array_crop)
    
    def thin(self, array, n, axis):

        width = array.shape[1]
        height = array.shape[0]
        i = 1
        if axis:
            while i * n < height:
                np.delete(array, i * n, 1)
                i += 1
        else:
            while i * n < width:
                np.delete(array, i * n, 0)
                i += 1

array = image.imread("../koala.png")
sb = ScrapBooker()
crop(array, (10, 10), (1, 1))
