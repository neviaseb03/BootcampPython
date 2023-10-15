import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headings = []
scores = []
links = []

for item in soup.find_all('span', class_='titleline'):
    heading = item.find('a')
    if heading:
        headings.append(heading.get_text())
        links.append(heading['href'])

for item in soup.find_all('span', class_='score'):
    scores.append(item.get_text())

print("Headings: ", headings)
print("Scores: ", scores)
print("Links: ", links)