from uuid import uuid3, uuid4, NAMESPACE_URL
from xmtrace import xmtrace

@xmtrace
def xm_os_uuid(lua, *args):
    return str(uuid3(NAMESPACE_URL, args[0]) if args else uuid4()).upper()
