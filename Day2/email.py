import re
text=input("Enter an email")
pattern="^(?!.*@(yahoo|hotmail)\.(com|in|org)$).*\S+@\S+\.(com|in|org)$"
if re.findall(pattern,text)!=[]:
    print("The email is Valid")
else:
    print("Invalid email")