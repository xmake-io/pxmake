from os import makedirs
from xmerrno import set_errno

def xm_os_mkdir(lua, ph):
    try:
        makedirs(ph, 0o755, True)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
