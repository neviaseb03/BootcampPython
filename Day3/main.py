import tkinter
from tkinter import font
window=tkinter.Tk()

window.title("My first GUI")
#window.geometry("500x200")
window.minsize(1000,500)
def printhello():
    #print("Hello")
    label1.config(text="Hey there!",font=("Ariel", 20))
label = tkinter.Label(window, text="This is My First GUI!!!")
label.place(x=34,y=45)
label1 = tkinter.Label(window, text="So Letzz Begin!!!", font=("Times New Roman", 20))
label1.pack(side="bottom")
button = tkinter.Button(window, text="Click Me",command=printhello)
button.pack()
window.mainloop()