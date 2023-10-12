import re

def is_valid_date(date_str):
    date_pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/\d{4}$'
    if not re.match(date_pattern, date_str):
        a="Invalid Date"
        return a
    
    month, day, year = map(int, date_str.split('/'))
    if year < 0000 or year > 9999:
        a="Invalid Date"
        return a
    if month in {1, 3, 5, 7, 8, 10, 12} and (day < 1 or day > 31):
        a="Invalid Date"
        return a
    if month in {4, 6, 9, 11} and (day < 1 or day > 30):
        a="Invalid Date"
        return a
    if month == 2 and (day < 1 or (day > 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else day > 28)):
        a="Invalid Date"
        return a
    

    b="Valid Date"
    return b


date1 = input("Enter a date")
print(is_valid_date(date1))  
  
