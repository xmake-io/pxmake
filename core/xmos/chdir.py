from os import chdir
from os.path import expanduser
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_chdir(lua, ph):
    try:
        chdir(expanduser(ph))
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
