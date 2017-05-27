from os.path import isdir
from xmtrace import xmtrace

@xmtrace
def xm_os_isdir(lua, ph):
    return isdir(ph)
