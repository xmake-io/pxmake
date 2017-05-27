from os import stat

def xm_os_mtime(lua, ph):
    try:
        return int(stat(ph).st_mtime)
    except OSError:
        return 0
