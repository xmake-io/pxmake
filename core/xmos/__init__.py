from functools import partial
from xmos.argv import xm_os_argv
from xmos.find import xm_os_find
from xmos.uuid import xm_os_uuid
from xmos.isdir import xm_os_isdir
from xmos.rmdir import xm_os_rmdir
from xmos.mkdir import xm_os_mkdir
from xmos.cpdir import xm_os_cpdir

def register(lua):
    lua.execute("os = os or {}")
    xmos = lua.globals().os
    xmos.argv = partial(xm_os_argv, lua)
    xmos.find = partial(xm_os_find, lua)
    xmos.uuid = partial(xm_os_uuid, lua)
    xmos.isdir = partial(xm_os_isdir, lua)
    xmos.rmdir = partial(xm_os_rmdir, lua)
    xmos.mkdir = partial(xm_os_mkdir, lua)
    xmos.cpdir = partial(xm_os_cpdir, lua)
