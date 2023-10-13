import random
import tkinter
from tkinter import font

window = tkinter.Tk()
window.title("My password generator")
window.minsize(650, 300)

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def fun():
    password_list = []
    nr_letters = int(input1.get())
    nr_symbols = int(input2.get())
    nr_numbers = int(input3.get())

    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    label4.config(text=f"Your newly generated password is {password}", font=("Arial", 20))

label = tkinter.Label(window, text="My Password Generator",font=("Arial", 30))
label.grid(row=0, column=10, padx=150,pady=20)

label1 = tkinter.Label(window, text="How many letters would you like in your password?")
label1.grid(row=2, column=10)
input1 = tkinter.Entry()
input1.grid(row=3, column=10)

label2 = tkinter.Label(window, text="How many symbols would you like?")
label2.grid(row=5, column=10)
input2 = tkinter.Entry()
input2.grid(row=6, column=10)

label3 = tkinter.Label(window, text="How many numbers would you like?")
label3.grid(row=8, column=10)
input3 = tkinter.Entry()
input3.grid(row=9, column=10)

button = tkinter.Button(window, text="Submit", command=fun)
button.grid(row=11, column=10,pady=20)

label4 = tkinter.Label(window, text="Letzzz Create a Password!!!")
label4.grid(row=12, column=10)

window.mainloop()
