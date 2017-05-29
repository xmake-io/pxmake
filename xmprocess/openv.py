from subprocess import Popen
from xmtrace import xmtrace
from xmerrno import set_errno
import xmprocess.procpool as procpool

@xmtrace
def xm_process_openv(lua, shellname, argv, outfile = None, errfile = None):
    try:
        return procpool.add(Popen([shellname] + list(argv.values()), stdout = open(outfile, "w") if outfile != None else None, stderr = open(errfile, "w") if errfile != None else None))
    except OSError as e:
        set_errno(e.errno)
        return None
