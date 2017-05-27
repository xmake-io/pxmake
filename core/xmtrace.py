def xmtrace(func):
    def newfunc(lua, *args):
        try:
            return func(lua, *args)
        except Exception:
            print(lua.globals().debug.traceback())
            raise
    return newfunc
