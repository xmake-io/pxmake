from os import listdir
from os.path import isdir

def xm_os_emptydir(lua, ph):
    return isdir(ph) and not listdir(ph)
