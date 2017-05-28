from xmtrace import xmtrace
from xmerrno import set_errno
from subprocess import TimeoutExpired

@xmtrace
def xm_process_wait(process, timeout = None):
    try:
        return 1, process.wait(timeout)
    except TimeoutExpired:
        return 0, 0
    except OSError as e:
        set_errno(e.errno)
        return 0, 0
