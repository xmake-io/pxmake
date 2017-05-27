from os.path import exists, expanduser
from xmtrace import xmtrace

@xmtrace
def xm_os_exists(lua, ph):
    return exists(expanduser(ph))
