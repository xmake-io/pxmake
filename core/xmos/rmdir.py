from shutil import rmtree
from os import rmdir
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_rmdir(lua, ph, *args):
    rmempty = True if args and args[0] == True else False
    try:
        if rmempty:
            rmdir(ph)
        else:
            rmtree(ph)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
