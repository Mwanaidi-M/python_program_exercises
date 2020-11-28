
import math
import os
import random
import re
import sys
import itertools


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    class Hourglass(object):
        hourglass = [[1, 1, 1],
                 [0, 1, 0],
                 [1, 1, 1]]

        def __init__(self, hourglass_shape=None):
            if hourglass_shape is not None:
                self.hourglass = hourglass_shape

        def count(self, info):
            i, j, array_ = info
            return sum([sum([a*b for a,b in zip(array_line[j:], hourglass_line)])
                    for array_line, hourglass_line in zip(array_[i:], 
                                                          self.hourglass)])

hourglass = Hourglass()

i_range = range(len(arr) - len(hourglass.hourglass) + 1)
# Assuming rectangular
j_range = range(len(arr[0]) - len(hourglass.hourglass[0]) + 1)

print(max(map(hourglass.count, itertools.product(i_range, j_range, [arr]))))
