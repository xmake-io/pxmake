from functools import partial
from xmstring.strcmp import xm_string_strcmp
from xmstring.startswith import xm_string_startswith
from xmstring.endswith import xm_string_endswith

def register(lua):
    lua.execute("string = string or {}")
    string = lua.globals().string
    string.strcmp = partial(xm_string_strcmp, lua)
    string.startswith = partial(xm_string_startswith, lua)
    string.endswith = partial(xm_string_endswith, lua)
