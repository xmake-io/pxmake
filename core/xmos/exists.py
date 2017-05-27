from os.path import exists
from xmtrace import xmtrace

@xmtrace
def xm_os_exists(lua, ph):
    return exists(ph)
