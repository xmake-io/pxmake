from os import path
from xmtrace import xmtrace
from xmbase import pathjoin

@xmtrace
def xm_path_absolute(lua, ph, root = None):
    return path.abspath(path.expanduser(ph)) if root == None else path.normpath(path.expanduser(pathjoin(root, ph)))
