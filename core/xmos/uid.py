from os import getresuid, setreuid
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_uid(lua, arg1 = None, arg2 = None):
    ruid = euid = None
    if arg1 != None and arg2 == None:
        if isinstance(arg1, int):
            ruid = euid = arg1
        else:
            ruid = arg1.ruid
            euid = arg1.euid
    elif arg1 != None and arg2 != None:
        ruid = arg1
        euid = arg2
    rv = {}
    if ruid != None or euid != None:
        try:
            setreuid(ruid if ruid != None else -1, euid if euid != None else -1)
            rv["errno"] = 0
        except OSError as e:
            set_errno(e.errno)
            rv["errno"] = e.errno
    rv["ruid"], rv["euid"], rv["suid"] = getresuid()
    return lua.table(**rv)
