from os import listdir
from os.path import isdir, expanduser
from xmtrace import xmtrace

@xmtrace
def xm_os_emptydir(lua, ph):
    ph = expanduser(ph)
    return isdir(ph) and not listdir(ph)
