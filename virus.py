from tkinter import *
foem tkinter import messagebox
window=Tk()
window.title("Virus")
window.geometry("300x200")
def virus():
    messagebox.showwarning("virus" "your computer is infected with a virus!")
 button=Button(window, text="scan for viruses", command=virus)
button.place(x=80, y=80)
window.mainloop()   