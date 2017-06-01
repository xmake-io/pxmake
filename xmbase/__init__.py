import os
from functools import reduce

def pathjoin(*args):
    return reduce(lambda a, b: a + os.sep + b, args)
