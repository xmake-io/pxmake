from xmtrace import xmtrace
from lupa import LuaSyntaxError

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
    try:
        while True:
            try:
                print('= ' + str(lua.execute(xm_sandbox_loadline())))
            except LuaSyntaxError as e:
                print(e)
            except KeyboardInterrupt:
                print("\nEOF or `os.exit()` to exit")
    except EOFError:
        pass
