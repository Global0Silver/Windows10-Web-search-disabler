import tkinter
import customtkinter
import winreg

#Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search
REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search"

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
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
    

def enable_ws():
    set_reg('BingSearchEnabled', str(1))
    finish_label.configure(text="Web search enabled")
def disable_ws():
    set_reg('BingSearchEnabled', str(0))
    finish_label.configure(text="Web search disabled")
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x115")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app,
                                 width=290,
                                 height=32,
                                 corner_radius=8,
                                 text="Disable web search",
                                 command=disable_ws)
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
button1 = customtkinter.CTkButton(master=app,
                                 width=290,
                                 height=32,
                                 corner_radius=8,
                                 text="Enable web search",
                                 command=enable_ws)
button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
finish_label = customtkinter.CTkLabel(app,justify='center', text="",text_color="green")
finish_label.place(rely=0.9, relx=0.5,anchor="center")

app.mainloop()
