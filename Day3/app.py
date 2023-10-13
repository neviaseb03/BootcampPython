import tkinter
from tkinter import font
window=tkinter.Tk()
window.title("My name")
window.minsize(1000,500)
label1 = tkinter.Label(window, text="Enter your name:")
label1.pack()
input = tkinter.Entry()
input.pack()
def fun():
    user_input =input.get()
    label2.config(text=user_input,font=("Ariel", 20))                   
label2 = tkinter.Label(window, text="Nevia Sebastian!!!", font=("Times New Roman", 20))
label2.pack(side="bottom")
button = tkinter.Button(window, text="Submit",command=fun)
button.pack()