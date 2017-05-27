from shutil import copytree
from xmerrno import set_errno

def xm_os_cpdir(lua, src, dst):
    try:
        copytree(src, dst)
    except OSError as e:
        set_errno(e.errno)
        return False
    return True
