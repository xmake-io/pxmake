from os.path import join
from re import split
from functools import reduce
from xmtrace import xmtrace

@xmtrace
def xm_path_translate(lua, ph):
    return reduce(join, split(r"\\|/", ph))
