from subprocess import Popen
from xmtrace import xmtrace
from xmerrno import set_errno

@xmtrace
def xm_process_openv(lua, shellname, argv, *args):
    outfile = args[0] if args and len(args) >= 1 else None
    errfile = args[1] if args and len(args) >= 2 else None
    try:
        return Popen([shellname] + argv, stdout = open(outfile, "w") if outfile != None else None, stderr = open(errfile, "w") if errfile != None else None)
    except OSError as e:
        set_errno(e.errno)
        return None
