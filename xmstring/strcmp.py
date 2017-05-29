from xmtrace import xmtrace

@xmtrace
def xm_string_strcmp(lua, s1, s2):
    return -1 if s1 < s2 else 1 if s2 < s1 else 0
