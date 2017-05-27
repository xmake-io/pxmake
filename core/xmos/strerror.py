import xmerrno
from os import strerror

def xm_os_strerror(lua):
    return strerror(xmerrno.errno)
