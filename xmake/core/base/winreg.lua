local winreg = winreg or {}
local _has_winreg, pywinreg = pypcall(pyimport, "winreg")

function winreg.query(keyname)
    if not _has_winreg then return nil, "import winreg error" end
    local rootkey_end = keyname:find("\\")
    if not rootkey_end then return nil, string.format("parse pathkey and pathsubkey failed: %s", keyname) end
    local r_value_end = keyname:reverse():find(";")
    if not r_value_end then r_value_end = 0 end
    rootkey = keyname:sub(1, rootkey_end - 1)
    if rootkey == "HKEY_CLASSES_ROOT" then rootkey = pywinreg.HKEY_CLASSES_ROOT
    elseif rootkey == "HKEY_CURRENT_CONFIG" then rootkey = pywinreg.HKEY_CURRENT_CONFIG
    elseif rootkey == "HKEY_CURRENT_USER" then rootkey = pywinreg.HKEY_CURRENT_USER
    elseif rootkey == "HKEY_LOCAL_MACHINE" then rootkey = pywinreg.HKEY_LOCAL_MACHINE
    elseif rootkey == "HKEY_USERS" then rootkey = pywinreg.HKEY_USERS
    else return nil, string.format("invalid registry path: %s", keyname) end
    local ok, rv = pypcall(function()
        key = pytypecall(pywinreg.OpenKey, {pyint, 0}, rootkey, keyname:sub(rootkey_end + 1, #keyname - r_value_end))
        val, tp = pywinreg.QueryValueEx(key, keyname:reverse():sub(1, math.max(0, r_value_end - 1)):reverse())
        key.Close()
        if tp == pywinreg.REG_SZ then return val end
        if tp == pywinreg.REG_EXPAND_SZ then return pywinreg.ExpandEnvironmentStrings(val) end
        if tp == pywinreg.REG_DWORD then return tostring(val) end
        if tp == pywinreg.REG_QWORD then return tostring(val) end
        return tp
    end)
    if not ok then return nil, string.format("get registry value failed: %s", keyname) end
    if type(rv) ~= "string" then return nil, string.format("unsupported registry value type: %d", rv) end
    return rv
end

return winreg
