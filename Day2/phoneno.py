import re
text=input("Enter an phone no:")
pattern="^\(\d{3}\)-\d{3}-\d{4}$"
if re.findall(pattern,text)!=[]:
    print("The phone no: is Valid")
else:
    print("Invalid phone no:..No: greater than 10")
    print("Checking for Country code")
    pattern1="\+[0-9]{2}\(\d{3}\)-\d{3}-\d{4}"
    if re.findall(pattern1,text)!=[]:
        print("The phone no: is Valid")
    else:
        print("Invalid phone no:")