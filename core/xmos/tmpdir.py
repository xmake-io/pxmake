from tempfile import gettempdir
from xmtrace import xmtrace

@xmtrace
def xm_os_tmpdir(lua):
    return gettempdir()
