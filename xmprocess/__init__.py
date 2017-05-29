from functools import partial
from xmprocess.openv import xm_process_openv
from xmprocess.wait import xm_process_wait
from xmprocess.waitlist import xm_process_waitlist
from xmprocess.close import xm_process_close

def register(lua):
    lua.execute("process = process or {}")
    xmprocess = lua.globals().process
    xmprocess.openv = partial(xm_process_openv, lua)
    xmprocess.wait = partial(xm_process_wait, lua)
    xmprocess.waitlist = partial(xm_process_waitlist, lua)
    xmprocess.close = partial(xm_process_close, lua)
