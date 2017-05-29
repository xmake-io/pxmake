from xmtrace import xmtrace

@xmtrace
def xm_string_startswith(lua, s1, s2):
    return s1.startswith(s2)
