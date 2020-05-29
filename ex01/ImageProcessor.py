import numpy as np
from matplotlib import image
from matplotlib import pyplot
from os import path

class ImageProcessor:
    def __init__(self):
        pass
    
    def load(self, path_file):
        if path.exists(path_file):
            array = np.array(image.imread(path_file))
            print("Shape of img : ({}, {})".format(array.shape[0], array.shape[1]))
            return array
        else:
            print("Path is incorrect")
            return None
    
    def display(self, array):
        try:
            image.imsave("img_create.png", array)
            img = pyplot.imread("img_create.png")
            pyplot.imshow(array)
            pyplot.show()
        except ValueError:
            print("Arg is not a numpy array")


ip = ImageProcessor()
print(ip.load("../koala.png"))
print(ip.load("zkjgoierkrfk,orj"))

array = ip.load("../koala.png")
ip.display(array)
ip.display(5)
