from xmtrace import xmtrace

@xmtrace
def xm_process_close(lua, process):
    process.terminate()
    return True
