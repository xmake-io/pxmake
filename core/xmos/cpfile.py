from shutil import copy2

def xm_os_cpfile(lua, src, dst):
    try:
        copy2(src, dst)
    except OSError:
        return False
    return True
