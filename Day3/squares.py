import tkinter
from tkinter import font
window=tkinter.Tk()
window.title("Squares")
window.minsize(300,150)
label1 = tkinter.Label(window, text="Enter a no:")
label1.grid(row=0, column=10)
input = tkinter.Entry()
input.grid(row=1, column=10)
def fun():
    user_input =float(input.get())
    i=user_input**2
    label2.config(text=f"Result: {i}",font=("Ariel", 20))                   
label2 = tkinter.Label(window, text="Squares", font=("Times New Roman", 20))
label2.grid(row=3, column=10)
button = tkinter.Button(window, text="Submit",command=fun)
button.grid(row=2, column=10)
window.mainloop()