from os.path import relpath
from xmtrace import xmtrace

@xmtrace
def xm_path_relative(lua, ph, *args):
    return relpath(ph, *args)
