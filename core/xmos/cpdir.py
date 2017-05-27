from shutil import copytree

def xm_os_cpdir(lua, src, dst):
    try:
        copytree(src, dst)
    except OSError:
        return False
    return True
