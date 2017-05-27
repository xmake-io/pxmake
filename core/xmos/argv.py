from shlex import split
from xmtrace import xmtrace

@xmtrace
def xm_os_argv(lua, args):
    arr = split(args)
    return lua.table(*arr)
