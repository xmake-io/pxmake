from os.path import isdir, expanduser
from xmtrace import xmtrace

@xmtrace
def xm_os_isdir(lua, ph):
    return isdir(expanduser(ph))
