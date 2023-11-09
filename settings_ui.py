import locale as loc
from logger import *
from tkinter import *
import json

#from TextConverterGUI import themeupdate

settings = ""
logging_var = ""
language_entry = ""
theme_var= ""
logging_checkbox = ""
language_label = ""
language_entry = ""
theme_label = ""
theme_light_radio = ""
theme_dark_radio = ""
save_button = ""
load_button = ""
set_theme_button = ""
current_theme = ""


def ui_settings(window):
    global logging_var
    global theme_var
    global logging_checkbox
    global language_label
    global language_entry
    global theme_label
    global theme_light_radio
    global theme_dark_radio
    global save_button
    global load_button
    global set_theme_button
    global current_theme

    settings=Tk()
    settings.title("Settings of Text Converter V2.3 [W.I.P]")
    settings.geometry("400x300")
    settings.resizable(width=False, height=False)

    logging_var = IntVar()
    logging_checkbox = Checkbutton(settings, text="Activate Logging?", variable=logging_var)
    logging_checkbox.pack()
    
    language_label = Label(settings, text="Language (DE/EN) (Not Working rn)")
    language_label.pack()
    language_entry = Entry(settings)
    language_entry.pack()
    
    theme_var = StringVar(value="dark")
    theme_label = Label(settings, text="Theme:")
    theme_label.pack()
    theme_light_radio = Radiobutton(settings, text="Light", variable=theme_var, value="light", command=lambda: theme_var.set("light"))
    theme_light_radio.pack()
    theme_dark_radio = Radiobutton(settings, text="Dark", variable=theme_var, value="dark", command=lambda:theme_var.set("dark"))
    theme_dark_radio.pack()

    # Create the button to save the settings
    save_button = Button(settings, text="Save Settings", command=save_settings)
    save_button.pack()
    
    load_button = Button(settings, text="Load Settings", command=lambda:load_settings(settings, window))
    load_button.pack()
    
    set_theme_button = Button(settings, text="Set Theme Temporarily", command=lambda:apply_theme(settings, window, (theme_var.get())))
    set_theme_button.pack()
    
    load_settings(settings, window)
    apply_theme(settings, window, current_theme)

#def language_ui()

# Define the function to save the settings
def save_settings():
    global current_theme
    # Get the settings from the entry widgets
    logging = logging_var.get()
    language = language_entry.get()
    theme = theme_var.get()

    # Create a dictionary of the settings
    settings = {
        "logging": logging,
        "language": language,
        "theme": theme,
    }

    # Write the settings to a file
    with open("settings.json", "w") as f:
        json.dump(settings, f)
    return

# Define the function to load the settings
def load_settings(settings, window):
    global current_theme
    # Read the settings from the file
    with open("settings.json", "r") as f:
        setting = json.load(f)
        
    current_theme = setting.get("theme")
    print(current_theme)
    apply_theme(settings, window, current_theme)
    return window
    
        
def apply_theme(settings, window, current_theme):
    print(current_theme)
    
    if current_theme=="light":
        settings.config(bg="#EFEFEF")
        logging_checkbox.config(bg="#EFEFEF", fg="black")
        language_label.config(bg="#EFEFEF", fg="black")
        language_entry.config(bg="#FFFFFF", fg="black")
        theme_label.config(bg="#EFEFEF", fg="black")
        theme_light_radio.config(bg="#EFEFEF", fg="black")
        theme_dark_radio.config(bg="#EFEFEF", fg="black")
        save_button.config(bg="#EFEFEF", fg="black")
        load_button.config(bg="#EFEFEF", fg="black")
        set_theme_button.config(bg="#EFEFEF", fg="black")
    if current_theme=="dark":
        settings.config(bg="#1F1F1F")
        logging_checkbox.config(bg="#1F1F1F", fg="#FFFFFF")
        language_label.config(bg="#1F1F1F", fg="#FFFFFF")
        language_entry.config(bg="#1F1F1F", fg="#FFFFFF")
        theme_label.config(bg="#1F1F1F", fg="#FFFFFF")
        theme_light_radio.config(bg="#1F1F1F", fg="#FFFFFF")
        theme_dark_radio.config(bg="#1F1F1F", fg="#FFFFFF")
        save_button.config(bg="#1F1F1F", fg="#FFFFFF")
        load_button.config(bg="#1F1F1F", fg="#FFFFFF")
        set_theme_button.config(bg="#1F1F1F", fg="#FFFFFF")
    #apply_theme_main(window, current_theme)
    return window

def apply_theme_main(window, current_theme):
    window.config(bg="#1F1F1F")
    return