from shutil import copy2
from xmerrno import set_errno
from xmtrace import xmtrace
from os.path import expanduser, dirname
from os import makedirs

@xmtrace
def xm_os_cpfile(lua, src, dst):
    try:
        src = expanduser(src)
        dst = expanduser(dst)
        makedirs(dirname(dst), 0o755, True)
        copy2(src, dst)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
