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
  print( "You enter the right path and end up bumping into some light from lava far ahead.\nYou see that there are again 2 paths, up or down next to a patch of lava illuminating the area.")	

P1B2 = tk.button(MCPAP, text="Go into the right", command=P1B2Click)
P1B2.pack()

Def P2B1Click(): 
  print("You decide to move upwards and don’t see any mobs.\nYou end up moving more forward and you see a skeleton by itself.\nThey catch you off guard and kill you, it happens")

P2B1 = tk.button(MCPAP, text="Go up", command=P2B1Click)
P2B1.pack()

Def P2B2Click():
  print("You decide to move downwards and you see an Enderman.\nKnowing what they do you avoid eye contact, something you’re probably used to.\nYou see diamonds nearby guarded by 3 skeletons and 2 zombies.")

P2B2 = tk.button(MCPAP, text="Go down", command=P2B2Click)

Def P3B1Click():
  print("You pull out your sword from muscle memory and you don’t take damage while dispatching the zombies.\nBy the time you move onto the skeletons your sword breaks, and you end up panicking.\nThe skeletons 2 shot you.\nPay more attention...")

P3B1 = tk.button(MCPAP, text="Fight (Sword)", command=P3B1Click)

Def P3B2Click():
  print("You decide to try waiting for the mobs to leave to save some materials and tools.\nYou wait for around 2 minutes when you suddenly hear hissing.\nThere’s a creeper behind you and it explodes you.\nNice social awareness you have...")

P3B2 = tk.button(MCPAP, text="Wait It Out", command=P3B2Click)

Def P3B3Click():
  print("You pull out your Axe from your real inventory because your sword is on low durability.\nYou end up sweeping all the mobs with 2 hearts left.")

P3B3 = tk.button(MCPAP, text="Fight (Axe)", command=P3B3Click)

Def P4BClick():
  print("You quickly create an iron pickaxe from materials left over from your save.\nYou end up mining 2 diamonds.\nYou end up going home, not empty handed.\nGood job.")

P4B = tk.button(MCPAP, text="Mine Diamonds", command=P4BClick)

MCPAP.mainloop()
