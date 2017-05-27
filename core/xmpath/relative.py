from os.path import relpath, expanduser
from xmtrace import xmtrace

@xmtrace
def xm_path_relative(lua, ph, *args):
    return relpath(expanduser(ph), *args)
