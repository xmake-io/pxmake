from os import getcwd
from xmtrace import xmtrace

@xmtrace
def xm_os_curdir(lua):
    return getcwd()
