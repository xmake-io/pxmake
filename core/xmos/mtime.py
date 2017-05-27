from os import stat
from xmerrno import set_errno

def xm_os_mtime(lua, ph):
    try:
        return int(stat(ph).st_mtime)
    except OSError as e:
        set_errno(e.errno)
        return 0
