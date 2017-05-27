from functools import partial
from xmos.argv import xm_os_argv
from xmos.find import xm_os_find
from xmos.uuid import xm_os_uuid

def register(lua):
    lua.execute("os = os or {}")
    xmos = lua.globals().os
    xmos.argv = partial(xm_os_argv, lua)
    xmos.find = partial(xm_os_find, lua)
    xmos.uuid = partial(xm_os_uuid, lua)
