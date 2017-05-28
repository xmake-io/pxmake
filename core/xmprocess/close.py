from xmtrace import xmtrace
import xmprocess.procpool as procpool

@xmtrace
def xm_process_close(lua, process):
    procpool.pool[process].terminate()
    procpool.pool[process] = None
    return True
