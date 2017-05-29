from xmtrace import xmtrace
from lupa import LuaSyntaxError, LuaError, lua_type
from sys import stdout

def xm_sandbox_loadline():
    lns = [input("> ")]
    if not lns[0]:
        return ''
    if lns[0][0] == '=':
        lns[0] = 'return' + lns[0][1:]
    while lns[-1][-1] == '\\':
        lns[-1] = lns[-1][:-1]
        lns.append(input(">> "))
    return '\n'.join(lns)

@xmtrace
def xm_sandbox_interactive(lua, instance):
    lgl = lua.globals()
    try:
        while True:
            try:
                rv = lgl.setfenv(lgl.loadstring(xm_sandbox_loadline()), instance)()
                print('= ', end = '')
                stdout.flush()
                if lua_type(rv) == 'table':
                    lgl.table.dump(rv)
                else:
                    lgl.print(rv)
            except (LuaSyntaxError, LuaError) as e:
                print(e)
            except KeyboardInterrupt:
                print("\nEOF or `os.exit()` to exit")
    except EOFError:
        pass
