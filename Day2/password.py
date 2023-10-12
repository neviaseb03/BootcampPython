import re

def is_strong_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

    if bool(re.match(pattern, password))==True:
        b="Valid Password"
    else:
        b="Invalid Password"
    return b
password1 = input("Enter a password")  
print(is_strong_password(password1)) 
