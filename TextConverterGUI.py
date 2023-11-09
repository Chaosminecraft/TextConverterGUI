#importing modules
import ctypes
import time
from converter_ui import ui_convert
from settings_ui import ui_settings
from tkinter import *
from threading import Thread, Event

#Variables 
window=""
error=""
operator=""
convert=""
deconvert=""
optionsVar=""
messageVar=""
mail="chaosminecraftmail@gmail.com"

#input variables
input_convert=""
input_deconvert=""

#temporary variables go here
stop_event = Event()

def convert_deconvert(input_convert, input_deconvert):
        show="mesage"
        if (convert.get()) == 1:
            content=input_convert.get()
            opt="convert"
            conv_thread=Thread(target=ui_convert, args=(operator, opt, content, show))
            conv_thread.start()
            #ui_convert(operator, opt, content, show) #legacy way if it doesn't work.
            return
        
        if (deconvert.get()) == 1:
            content=input_deconvert.get()
            opt="deconvert"
            deconv_thread=Thread(target=ui_convert, args=(operator, opt, content, show))
            deconv_thread.start()
            #ui_convert(operator, opt, content, show) #legacy way if it doesn't work.
            return

def main():
    global window
    global input_convert
    global input_deconvert
    global optionsVar
    global messageVar
    global convert
    global deconvert

    try:
        window=Tk()
        window.config(bg="#EFEFEF")
        window.title("Text Converter V2.3 UI Preview [W.I.P]")
        window.geometry("600x500")
        window.resizable(width=False, height=False)
        
        deconvert_msg=Label(window, text="Text to deconvert:", padx=5, pady=5)
        deconvert_msg.place(x=160, y=0)

        convert_msg=Label(window, text="Text to convert:", padx=5, pady=5)
        convert_msg.place(x=160, y=35)

        input_deconvert=Entry(window, width=50)
        input_deconvert.place(x=160, y=20)

        input_convert=Entry(window, width=50)
        input_convert.place(x=160, y=60)

        settings_warn=Label(window, text="This settings Window may not work in the Beta Version!")
        settings_warn.place(x=70, y=100)
        
        convert=IntVar()
        
        convert_check=Checkbutton(window, text="Convert", relief="raised", onvalue=1, offvalue=0, variable=convert)
        convert_check.place(x=70, y=57)
        
        deconvert=IntVar()
        
        deconvert_check=Checkbutton(window, text="Deconvert", relief="raised", onvalue=1, offvalue=0, variable=deconvert)
        deconvert_check.place(x=70, y=17)

        convert_butt=Button(window, text="Go.", padx=5, pady=5, command=lambda:convert_deconvert(input_convert, input_deconvert))
        convert_butt.place(x=70, y=120)

        settings_butt=Button(window, text="Settings", padx=5, pady=5, command=lambda:ui_settings(window))
        settings_butt.place(x=115, y=120) 

        exit_butt=Button(window, text="Exit", pady=5, padx=5, command=ui_exit)
        exit_butt.place(x=185, y=120)

        optionsVar=StringVar(window)
        optionsVar.set("Hex")
        options=OptionMenu(window, optionsVar, "Hex", "Pseudo Hex", "Binary", "Pseudo Binary", "Legacy Pseudo Binary", "ascii", "leetspeak", "brainfuck", "base64")
        options.place(x=220, y=160)
        

        messageVar=StringVar(window)
        messageVar.set("Messageview")
        messageview=OptionMenu(window, messageVar, "Messageview", "QR Code")
        messageview.place(x=70, y=160)

        warning_label=Label(window, text="↑ Warning: the QR Code can't be Viewed and only Generated!")
        warning_label.place(x=110, y=280)

        #testthread=Thread(target=TempLoop)
        #testthread.start()

        window.mainloop()
    except SystemExit:
        return

def TempLoop():
    global stop_event
    while not stop_event.is_set():
        try:
            optionsVar = optionsVar.get()
            messageVar = messageVar.get()
            print(optionsVar, messageVar)
            time.sleep(1)
        except UnboundLocalError:
            print("A Variable is Fucked.")

def ui_exit():
    global stop_event
    result=ctypes.windll.user32.MessageBoxW(0, "If you press Ok, the Program will close, but if you press Cancel it stays open.", "Do you wanna close that?", 1)
    if result == 1:
        stop_event.set()
        exit()
    else:
        return

main()

def themeupdate(current_theme):
    PutCodeHere=""
    return