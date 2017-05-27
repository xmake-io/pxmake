from os.path import relpath

def xm_path_relative(lua, ph, *args):
    return relpath(ph, *args)
