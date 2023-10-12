import re
pattern = r"https?://(www\d*\.)?([a-zA-Z0-9.-]+)(/.*)?"

url = input("Enter an URL")
match = re.search(pattern, url)
if match:
    domain = match.group(2)  
    print("Domain:", domain)
else:
    print("No domain found in the URL.")