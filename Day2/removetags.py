import re

def removetags(string):
    pattern = r'<.*?>'
    clean_str = re.sub(pattern, '', string)
    return clean_str
html_string = input("Enter a sentence")
clean = removetags(html_string)
print(clean)