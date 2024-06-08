import winreg
#Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings
REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings"

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
print ("Disable web search > 1")
print ("Enable web search  > 2")
user_choice = input (">")
if user_choice == "1":
 set_reg('IsGlobalWebSearchProviderToggleEnabled', 0)
else:
 set_reg('IsGlobalWebSearchProviderToggleEnabled', 1)
#Read value and double check    
if (get_reg('IsGlobalWebSearchProviderToggleEnabled')) == 0:
    print ("Web search disabled")
else:
    print ("Web search enabled")
