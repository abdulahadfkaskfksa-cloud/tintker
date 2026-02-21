from tkinter import *
window =Tk()
window.tile("Tkinter Grid Layout")
window.geometry("300x200")
for i in range(3):
    for J in range(3):
      frame=Frame(window, width=100, height=100, bg="red")
      frame.grid(row=1, column=J,padx=5 , pady=5)  
      label=Label(frame,text=f"Row {1} column {J}", FG="White", bg="red")
      label.pack()
window.mainloop()