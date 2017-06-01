from os.path import expanduser
from os import sep
from re import split
from functools import reduce
from xmtrace import xmtrace

@xmtrace
def xm_path_translate(lua, ph):
    return expanduser(reduce(lambda a, b: a + sep + b, split(r"\\|/", ph)))
