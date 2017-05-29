from functools import partial
from xmsandbox.interactive import xm_sandbox_interactive

def register(lua):
    lua.execute("sandbox = sandbox or {}")
    xmsandbox = lua.globals().sandbox
    xmsandbox.interactive = partial(xm_sandbox_interactive, lua)
