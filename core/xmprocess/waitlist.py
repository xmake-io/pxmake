from threading import Thread
from xmtrace import xmtrace
from xmerrno import set_errno
from subprocess import TimeoutExpired
import xmprocess.procpool as procpool

@xmtrace
def xm_process_waitlist(lua, proclist, timeout = None):
    if timeout < 0: timeout = None
    proclist = [(x, procpool.pool[x]) for x in proclist.values()]
    rvlist = [None] * len(proclist)
    def waitprocess(proc, index):
        try:
            rvlist[index] = [proc[0], index + 1, proc[1].wait(timeout)]
        except TimeoutExpired:
            pass
        except OSError as e:
            set_errno(e.errno)
            rvlist[index] = -1
    thlist = [Thread(target = lambda: waitprocess(proc, idx)) for idx, proc in enumerate(proclist)]
    for th in thlist:
        th.start()
    for th in thlist:
        th.join()
    if -1 in rvlist:
        return -1, None
    rvlist = [lua.table(*item) for item in rvlist if item != None]
    if len(rvlist) == 0:
        return 0, None
    return len(rvlist), lua.table(*rvlist)
