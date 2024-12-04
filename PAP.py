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

Def P1B1Click():
  print("You take 10 steps into the left path, you don’t pay attention and end up falling into lava.\nNice one.")

P1B1 = tk.button(MCPAP, text="Go into the left", command=P1B1Click)
P1B1.pack()

Def P1B2Click():
  print( "You enter the right path and end up bumping into some light from lava far ahead./nYou see that there are again 2 paths, up or down next to a patch of lava illuminating the area.")	

P1B2 = tk.button(MCPAP, text="Go into the right", command=P1B2Click)
P1B2.pack()

Def P2B1Click(): 
  print("You decide to move upwards and don’t see any mobs. You end up moving more forward and you see a skeleton by itself."






P2Label = tk.label(MCPAP, text="
MCPAP.mainloop()
