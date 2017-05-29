import readline

def register(lua):
    lua.execute("readline = readline or {}")
    xmreadline = lua.globals().readline
    xmreadline.readline = input
    xmreadline.history_list = lambda: lua.table(*[lua.table(line = readline.get_history_item(i)) for i in range(1, readline.get_current_history_length() + 1)])
    xmreadline.add_history = readline.add_history
    xmreadline.clear_history = readline.clear_history
