from os import remove
from xmerrno import set_errno

def xm_os_rmfile(lua, ph):
    try:
        remove(ph)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
