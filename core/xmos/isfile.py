from os.path import isfile

def xm_os_isfile(lua, ph):
    try:
        return isfile(ph)
    except OSError:
        return False
