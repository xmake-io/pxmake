from os import environ
from xmtrace import xmtrace

@xmtrace
def xm_os_setenv(lua, name, value):
    environ[name] = value
    return True
