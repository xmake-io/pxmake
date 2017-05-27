import os
from os import path

def xm_os_find(lua, rootdir, pattern, recurse, mode, *args):
    excludes = list(args[0].values()) if args else []
    lgl = lua.globals()
    def judge(phs):
        res = []
        for ph in phs:
            if mode == 1 and path.isdir(ph) or mode == 0 and path.isfile(ph) or mode not in (0, 1):
                if ph.startswith("./"):
                    ph = ph[2:]
                match = lgl.string.match
                if ph == match(ph, pattern):
                    rootlen = len(rootdir)
                    assert(rootdir != ph)
                    assert(rootlen + 1 <= len(ph))
                    phtk = ph[rootlen + 1:]
                    excluded = False
                    for exclude in excludes:
                        if match(phtk, exclude) == phtk:
                            excluded = True
                            break
                    if not excluded:
                        res.append(ph)
        return res
    if not recurse:
        res = judge([path.join(rootdir, nm) for nm in os.listdir(rootdir)])
    else:
        tree = []
        for (dirpath, dirnames, filenames) in os.walk(rootdir):
            tree += [path.join(dirpath, nm) for nm in dirnames + filenames]
        res = judge(tree)
    return lua.table(*res), len(res)
