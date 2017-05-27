from tempfile import gettempdir

def xm_os_tmpdir(lua):
    return gettempdir()
