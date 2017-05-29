from shutil import get_terminal_size
from xmtrace import xmtrace

@xmtrace
def xm_os_getwinsize(lua):
    size = get_terminal_size((-1, -1))
    return lua.table(width = size.columns, height = size.lines)
