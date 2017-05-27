def register(lua):
    lgl = lua.globals()
    original_xpcall = lgl.xpcall
    lgl.xpcall = lambda func, errfunc, *args: original_xpcall(lambda: func(*args), errfunc)
