def register(lua):
    lua.execute("original_xpcall = xpcall")
    lua.execute("function xpcall(func, errfunc, ...) local args = {...}; return original_xpcall(function() return func(unpack(args)) end, errfunc) end")
