number = int(input("Enter a number to generate a multiplication table: "))

print(f"Multiplication table for {number}:")

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")