from shlex import split
from xmtrace import xmtrace
import os

@xmtrace
def xm_os_argv(lua, args):
    arr = split(args, posix = os.name == "posix")
    return lua.table(*arr)
