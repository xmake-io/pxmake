from xmtrace import xmtrace
import xmprocess.procpool as procpool
from xmerrno import set_errno

@xmtrace
def xm_process_close(lua, process):
    if not procpool.pool[process]:
        return False
    try:
        procpool.pool[process].terminate()
        procpool.pool[process] = None
        return True
    except OSError as e:
        set_errno(e.errno)
        return False
