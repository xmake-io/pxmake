from importlib import import_module

def register(lua):
    lgl = lua.globals()
    lgl.pyimport = import_module
    def pypcall(func, *args):
        try:
            return True, func(*args)
        except Exception as e:
            return False, e
    lgl.pypcall = pypcall
    lgl.pylist = lambda table: list(table.values())
    lgl.pytuple = lambda table: tuple(table.values())
    lgl.pydict = lambda table: dict(table.items())
    lgl.pyprint = print
    lgl.pyluatable = lua.table_from
    lgl.pytypecall = lambda func, types, *args: func(*map(lambda tp, vl: tp(vl), types.values(), args))
    lgl.pyint = int
    lgl.pyfloat = float
    lgl.pytype = type
