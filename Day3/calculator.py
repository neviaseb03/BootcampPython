import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Basic Calculator")

display = tk.Entry(window, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)


buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

val1 = 1
val2 = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, height=2, command=calculate).grid(row=val1, column=val2)
    elif button == "C":
        tk.Button(window, text=button, width=10, height=2, command=lambda b=button: display.delete(0, tk.END)).grid(row=val1, column=val2)
    else:
        tk.Button(window, text=button, width=10, height=2, command=lambda b=button: button_click(b)).grid(row=val1, column=val2)

    val2 += 1
    if val2 > 3:
        val2 = 0
        val1 += 1

window.mainloop()
