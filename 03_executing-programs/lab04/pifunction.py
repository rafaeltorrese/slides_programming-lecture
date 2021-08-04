import math
import random


def inside_circle():
    R1, R2 = random.random(), random.random()
    return math.sqrt(R1 ** 2 + R2 ** 2) < 1