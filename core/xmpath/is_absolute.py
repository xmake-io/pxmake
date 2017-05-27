from os.path import isabs
from xmtrace import xmtrace

@xmtrace
def xm_path_is_absolute(lua, ph):
    return isabs(ph)
