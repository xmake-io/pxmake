from os import makedirs

def xm_os_mkdir(lua, ph):
    try:
        makedirs(ph, 0o755, True)
    except OSError:
        return False
    return True
