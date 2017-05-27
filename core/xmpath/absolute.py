from os import path
from xmtrace import xmtrace

@xmtrace
def xm_path_absolute(lua, ph, *args):
    return path.abspath(ph) if not args else path.normpath(path.join(args[0], ph))
