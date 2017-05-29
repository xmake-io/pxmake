pool = {}
count = 0
def add(proc):
    global pool, count
    pool[count] = proc
    count += 1
    return count - 1
