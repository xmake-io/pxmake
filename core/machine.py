import lupa
from lupa import LuaRuntime
from sys import argv, platform
from platform import python_version_tuple, machine
import os
import xmos
import xmpath
import xmstring
import xmprocess

def xm_version():
    return {
        "major": 2,
        "minor": 1,
        "alter": 5,
        "build": 0,
    }

def xm_machine_save_arguments(impl, argc, argv):
    lgl = impl["lua"].globals()
    lgl._ARGV = impl["lua"].table(*argv)

def xm_machine_get_project_directory(impl):
    lgl = impl["lua"].globals()
    lgl._PROJECT_DIR = path = os.path.abspath(os.getenv("XMAKE_PROJECT_DIR")) if os.getenv("XMAKE_PROJECT_DIR") else os.getcwd()
    return path

def xm_machine_get_program_file(impl):
    pass

def xm_machine_get_program_directory(impl):
    lgl = impl["lua"].globals()
    lgl._PROGRAM_DIR = path = os.path.abspath(os.getenv("XMAKE_PROGRAM_DIR"))
    return path

def xm_machine_init():
    impl = {"lua": LuaRuntime(unpack_returned_tuples=True)}
    lgl = impl["lua"].globals()
    xmos.register(impl["lua"])
    xmpath.register(impl["lua"])
    xmstring.register(impl["lua"])
    xmprocess.register(impl["lua"])
    pvt = python_version_tuple()
    assert(pvt[0] == '3' and int(pvt[1]) >= 3)
    if platform in ("win32", "cygwin"):
        lgl._HOST = "windows"
    elif platform == "darwin":
        lgl._HOST = "macosx"
    elif platform == "linux":
        lgl._HOST = "linux"
    elif os.name == "posix":
        lgl._HOST = "unix"
    else:
        lgl._HOST = "unknown"
    lgl._ARCH = machine()
    if platform == "win32":
        lgl._NULDEV = "nul"
    else:
        lgl._NULDEV = "/dev/nul"
    version = xm_version()
    lgl._VERSION = "%d.%d.%d.%d" % (version["major"], version["minor"], version["alter"], version["build"])
    lgl._VERSION_SHORT = "%d.%d.%d" % (version["major"], version["minor"], version["alter"])
    impl["lua"].execute("xmake={}")
    return impl

def xm_machine_main(impl, argc, argv):
    lgl = impl["lua"].globals()
    xm_machine_save_arguments(impl, argc, argv)
    xm_machine_get_project_directory(impl)
    xm_machine_get_program_file(impl)
    path = xm_machine_get_program_directory(impl)
    path += "/core/_xmake_main.lua"
    lgl.dofile(path)
    return lgl._xmake_main()

if __name__ == "__main__":
    machine = xm_machine_init()
    exit(xm_machine_main(machine, len(argv), argv))
