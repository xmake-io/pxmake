from functools import partial
from xmpath.relative import xm_path_relative

def register(lua):
    lua.execute("path = path or {}")
    xmpath = lua.globals().path
    xmpath.relative = partial(xm_path_relative, lua)
