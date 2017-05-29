from os import stat
from os.path import expanduser
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_getown(lua, ph):
    try:
        sts = stat(expanduser(ph))
        return lua.table(uid = sts.st_uid, gid = sts.st_gid)
    except OSError as e:
        set_errno(e.errno)
