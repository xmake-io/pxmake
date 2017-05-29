from xmtrace import xmtrace
from xmversion import xm_version
from platform import python_version_tuple

@xmtrace
def xm_os_versioninfo(lua):
    lgl = lua.globals()
    try:
        __import__("readline")
        features = lua.table(readline = True)
    except ImportError:
        features = lua.table()
    python_version = {}
    python_version["major"], python_version["minor"], python_version["alter"] = python_version_tuple()
    return lua.table(arch = lgl._ARCH, features = features, nuldev = lgl._NULDEV, host = lgl._HOST, version = lua.table(python = lua.table(**python_version), **xm_version()))
