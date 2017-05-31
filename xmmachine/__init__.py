import lupa
from lupa import LuaRuntime
from sys import argv, platform
from platform import python_version_tuple, machine
from re import fullmatch
import os
from xmversion import xm_version
import xmbuiltins
import xmos
import xmpath
import xmstring
import xmprocess
import xmsandbox
try:
    import xmreadline
except ImportError:
    pass

def xm_machine_save_arguments(impl, argc, argv):
    lgl = impl["lua"].globals()
    lgl._ARGV = impl["lua"].table(*argv[1:])

def xm_machine_get_project_directory(impl):
    lgl = impl["lua"].globals()
    lgl._PROJECT_DIR = path = os.path.abspath(os.getenv("XMAKE_PROJECT_DIR")) if os.getenv("XMAKE_PROJECT_DIR") else os.getcwd()
    return path

def xm_machine_get_program_file(impl):
    pass

def xm_machine_get_program_directory(impl):
    lgl = impl["lua"].globals()
    lgl._PROGRAM_DIR = path = os.path.abspath(os.getenv("XMAKE_PROGRAM_DIR")) if os.getenv("XMAKE_PROGRAM_DIR") else os.path.abspath(os.path.join(__file__, "..", "..", "xmake"))
    return path

def xm_machine_init():
    impl = {"lua": LuaRuntime(unpack_returned_tuples=True)}
    lgl = impl["lua"].globals()
    xmbuiltins.register(impl["lua"])
    xmos.register(impl["lua"])
    xmpath.register(impl["lua"])
    xmstring.register(impl["lua"])
    xmprocess.register(impl["lua"])
    xmsandbox.register(impl["lua"])
    try:
        xmreadline.register(impl["lua"])
    except (NameError, AttributeError):
        pass
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
    lgl._ARCH = "i386" if fullmatch(r'i\d86', machine()) else machine()
    lgl._NULDEV = os.devnull
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

def main():
    pvt = python_version_tuple()
    assert(pvt[0] == '3' and int(pvt[1]) >= 4)
    machine = xm_machine_init()
    return xm_machine_main(machine, len(argv), argv)
