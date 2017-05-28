from xmtrace import xmtrace
from machine import xm_version

@xmtrace
def xm_os_versioninfo(lua):
    lgl = lua.globals()
    try:
        __import__("readline")
        features = lua.table(readline = True)
    except ImportError:
        features = lua.table()
    return lua.table(arch = lgl._ARCH, features = features, nuldev = lgl._NULDEV, host = lgl._HOST, version = lua.table(**xm_version()))
