from functools import partial
from xmpath.relative import xm_path_relative
from xmpath.absolute import xm_path_absolute
from xmpath.translate import xm_path_translate
from xmpath.is_absolute import xm_path_is_absolute

def register(lua):
    lua.execute("path = path or {}")
    xmpath = lua.globals().path
    xmpath.relative = partial(xm_path_relative, lua)
    xmpath.absolute = partial(xm_path_absolute, lua)
    xmpath.translate = partial(xm_path_translate, lua)
    xmpath.is_absolute = partial(xm_path_is_absolute, lua)
