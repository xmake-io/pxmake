from uuid import uuid3, uuid4, NAMESPACE_URL
from xmtrace import xmtrace

@xmtrace
def xm_os_uuid(lua, string = None):
    return str(uuid3(NAMESPACE_URL, string) if string != None else uuid4()).upper()
