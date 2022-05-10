from re import X
import tkinter as tk
import button_commands

# creation of the main window
mainWindow = tk.Tk()
mainWindow.geometry("1000x600")

calcButton = tk.Button(mainWindow, text = "clac", height = 5, width = 20, command = lambda: print(button_commands.a))
calcButton.place(x = 100, y = 100)

mainWindow.mainloop()

