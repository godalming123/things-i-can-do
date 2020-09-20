from tkinter import *
win = Tk ()
win.attributes ("-alpha", 0.5)
list1 = Listbox (win)
list1.insert (1, "php")
list1.insert (2, "tkinter")
list1.insert (3, "pyhton")
list1.place (x =  200, y = 0)
for rank in range(8):
   for file in range(8):
      Label(win, text = str (rank) + str (file) + "|", borderwidth=1 ).grid(row = file  ,column = rank)
win.mainloop ()
