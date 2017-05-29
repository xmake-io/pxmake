from xmtrace import xmtrace
from lupa import LuaSyntaxError, LuaError

def xm_sandbox_loadline():
    lns = [input("> ")]
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
                print('= ' + str(lgl.setfenv(lgl.loadstring(xm_sandbox_loadline()), instance)()))
            except (LuaSyntaxError, LuaError) as e:
                print(e)
            except KeyboardInterrupt:
                print("\nEOF or `os.exit()` to exit")
    except EOFError:
        pass
