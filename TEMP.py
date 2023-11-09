import json
import tkinter as tk

# Define the function to save the settings
def save_settings():
    # Get the settings from the entry widgets
    logging = username_entry.get()
    language = remember_me_var.get()
    System = theme_var.get()

    # Create a dictionary of the settings
    settings = {
        "Wanna logg ": logging,
        "remember_me": language,
        "theme": System
    }

    # Write the settings to a file
    with open("settings.json", "w") as f:
        json.dump(settings, f)

# Define the function to load the settings
def load_settings():
    # Read the settings from the file
    with open("settings.json", "r") as f:
        settings = json.load(f)

    # Update the values of the widgets
    username_entry.delete(0, tk.END)
    username_entry.insert(0, settings["Wanna logg "])
    remember_me_var.set(settings["remember_me"])
    theme_var.set(settings["theme"])

# Create the Tkinter window
root = tk.Tk()

# Create the entry widgets for the settings
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

remember_me_var = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(root, text="Remember me", variable=remember_me_var)
remember_me_checkbox.pack()

theme_var = tk.StringVar(value="light")
theme_label = tk.Label(root, text="Theme:")
theme_label.pack()
theme_light_radio = tk.Radiobutton(root, text="Light", variable=theme_var, value="light")
theme_light_radio.pack()
theme_dark_radio = tk.Radiobutton(root, text="Dark", variable=theme_var, value="dark")
theme_dark_radio.pack()

# Create the button to save the settings
save_button = tk.Button(root, text="Save Settings", command=save_settings)
save_button.pack()

# Load the settings
load_settings()

# Start the Tkinter event loop
root.mainloop()