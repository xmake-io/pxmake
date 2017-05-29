from os import makedirs
from os.path import expanduser
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_mkdir(lua, ph):
    try:
        makedirs(expanduser(ph), 0o755, True)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
