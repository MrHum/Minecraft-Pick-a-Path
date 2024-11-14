import tkinter as tk 
MCPAP = tk.TK()
MCPAP.geometry("800 x 720") 
TitleIMG = tk.
TitleLabel = tk.label(MCPAP, text="Minecraft Pick-A-Path")
TitleLabel.pack()

StartB = tk.button(MCPAP, text="Press to Start")
StartB.pack()

P1Label = tk.label(MCPAP, text="You entered a cave you haven't explored before\nThere are two paths awaiting you\nDo you go left or right?")
P1Label.pack()

P1B1 = tk.button(MCPAP, text="Go left")
P1B1.pack()

P1B2 = tk.button(MCPAP, text="Go right")
P1B2.pack()

MCPAP.mainloop()
