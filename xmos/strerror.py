import xmerrno
from os import strerror
from xmtrace import xmtrace

@xmtrace
def xm_os_strerror(lua):
    return strerror(xmerrno.errno)
