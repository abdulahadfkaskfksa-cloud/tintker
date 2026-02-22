from tkinter import *
root = Tk()
root. title("Top Level window")
def open_window():
    top=Toplevel()
    top.title("top level window")
    top.geometry("200x100")
    12=Label(top, text="This is a top level window")
    12.pack(pady=20)
    top.mainloop

    13=Label(root, text="this is the main window")

    button=Button(root,text="open New Window", command=open_window)
    13.pack(pady=20)
    button.pack(pady=20)
    root.mainloop()    