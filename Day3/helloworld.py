import tkinter 

window = tkinter.Tk()
window.title("Hello, World!") 
window.minsize(200, 100)
label = tkinter.Label(window, text="Hello, World!", font=("Arial", 24))
label.pack(pady=20)  

window.mainloop()