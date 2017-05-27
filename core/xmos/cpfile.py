from shutil import copy2
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_cpfile(lua, src, dst):
    try:
        copy2(src, dst)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
