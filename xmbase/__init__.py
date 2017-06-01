import os
from functools import reduce

def pathjoin(*args):
    return os.sep.join(args)
