from os.path import isabs, expanduser
from xmtrace import xmtrace

@xmtrace
def xm_path_is_absolute(lua, ph):
    return isabs(expanduser(ph))
