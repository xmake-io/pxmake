from os.path import getmtime
from xmerrno import set_errno

def xm_os_mtime(lua, ph):
    try:
        return int(getmtime(ph))
    except OSError as e:
        set_errno(e.errno)
        return 0
