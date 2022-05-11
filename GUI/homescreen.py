from re import X
import tkinter as tk
import GUI.button_commands as buttons

# creation of the main window
mainWindow:tk.Tk 

def intialize():
    mainWindow = tk.Tk()
    mainWindow.geometry("1000x600")
    
    calcButton = tk.Button(mainWindow, text = "clac", height = 5, width = 20, command = lambda: buttons.print1(234))
    calcButton.place(x = 100, y = 100)
    
    mainWindow.mainloop()


