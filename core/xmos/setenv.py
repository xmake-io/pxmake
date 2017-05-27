from os import environ

def xm_os_setenv(lua, name, value):
    environ[name] = value
    return True
