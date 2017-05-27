from os import chdir

def xm_os_chdir(lua, ph):
    try:
        chdir(ph)
    except OSError:
        return False
    return True
