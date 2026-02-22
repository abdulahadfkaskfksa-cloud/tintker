from  tkinter import *
from  PTL import Image, ImageTk
window = Tk()
window.title("Tinker image")
window.geometry("300x200")

uplod= Image.open("background.jpg")
iamge= Image.photoimage(upload)
label=Label(window, iamge=image,height=350, width=350)
label.place(x=50, y=0)
label12=Label(window, text="welcome to Tinker Iamge", font=("Arial",16), bg="white")
label12.(x=40, y=360)
window.mainloop()