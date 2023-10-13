class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Division by zero is not allowed"
        return x / y

calculator = Calculator()

while True:
    print("*****MENU*****:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    user_input = int(input("Enter a choice: "))

    if user_input == 5:
        break
    elif user_input in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == 1:
            print("Sum:", calculator.add(num1, num2))
        elif user_input == 2:
            print("Difference:", calculator.subtract(num1, num2))
        elif user_input == 3:
            print("Product:", calculator.multiply(num1, num2))
        elif user_input == 4:
            print("Quotient:", calculator.divide(num1, num2))
    else:
        print("Invalid input. Please try again.")