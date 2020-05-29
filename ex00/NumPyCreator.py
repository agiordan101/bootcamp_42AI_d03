import numpy as np
from numbers import Real
import random


class NumPyCreator:
    def __init__(self):
        pass
    
    def from_list(self, lst):
        if isinstance(lst, list):
            return np.array(lst)
        else:
            return None

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple):
            return np.array(tpl)
        else:
            return None

    def from_iterable(self, itr):
        lst = []
        for i in itr:
            lst.append(i)
        return np.array(lst)

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            print("ERROR Type. Need tuple")
            quit()
        lst = []
        toadd = value
        for i in range(len(shape)):
            lst = []
            for j in range(shape[len(shape) - 1 - i]):
                lst.append(toadd)
            toadd = lst
        return self.from_list(lst)

    def random(self, shape):
        if not isinstance(shape, tuple):
            print("ERROR Type. Need tuple")
            quit()
        return np.random.random_sample(shape)

    def identity(self, n):
        if not isinstance(n, int):
            print("ERROR Type. Need integer")
            quit()
        return np.identity(n)


npc = NumPyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))

shape = (3, 3, 5)
print(npc.from_shape(shape))
shape = ()
print(npc.from_shape(shape))

shape = (3, 3, 5)
print(npc.random(shape))
print(npc.identity(4))
