from os import getresgid, setregid
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_gid(lua, arg1 = None, arg2 = None):
    rgid = egid = None
    if arg1 != None and arg2 == None:
        if isinstance(arg1, int):
            rgid = egid = arg1
        else:
            rgid = arg1.rgid
            egid = arg1.egid
    elif arg1 != None and arg2 != None:
        rgid = arg1
        egid = arg2
    rv = {}
    if rgid != None or egid != None:
        try:
            setregid(rgid if rgid != None else -1, egid if egid != None else -1)
            rv["errno"] = 0
        except OSError as e:
            set_errno(e.errno)
            rv["errno"] = e.errno
    rv["rgid"], rv["egid"], rv["sgid"] = getresgid()
    return lua.table(**rv)
