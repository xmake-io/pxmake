from os import remove

def xm_os_rmfile(lua, ph):
    try:
        remove(ph)
    except OSError:
        return False
    return True
