from os.path import getmtime, expanduser
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_mtime(lua, ph):
    try:
        return int(getmtime(expanduser(ph)))
    except OSError as e:
        set_errno(e.errno)
        return 0
