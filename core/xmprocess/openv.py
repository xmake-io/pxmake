from subprocess import Popen
from xmtrace import xmtrace
from xmerrno import set_errno

@xmtrace
def xm_process_openv(lua, shellname, argv, outfile = None, errfile = None):
    try:
        return Popen([shellname] + argv, stdout = open(outfile, "w") if outfile != None else None, stderr = open(errfile, "w") if errfile != None else None)
    except OSError as e:
        set_errno(e.errno)
        return None
