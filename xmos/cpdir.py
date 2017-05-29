from shutil import copytree
from xmerrno import set_errno
from xmtrace import xmtrace
from os.path import expanduser

@xmtrace
def xm_os_cpdir(lua, src, dst):
    try:
        copytree(expanduser(src), expanduser(dst))
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
