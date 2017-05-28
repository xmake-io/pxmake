from xmtrace import xmtrace
from xmerrno import set_errno
from subprocess import TimeoutExpired
import xmprocess.procpool as procpool

@xmtrace
def xm_process_wait(lua, process, timeout = None):
    if timeout < 0: timeout = None
    process = procpool.pool[process]
    try:
        return 1, process.wait(timeout)
    except TimeoutExpired:
        return 0, 0
    except OSError as e:
        set_errno(e.errno)
        return 0, 0
