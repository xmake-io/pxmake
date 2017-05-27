from shlex import split

def xm_os_argv(lua, args):
    arr = split(args)
    return lua.table(*arr)
