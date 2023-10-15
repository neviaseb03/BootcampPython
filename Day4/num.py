from bs4 import BeautifulSoup
file=open("index.html")
contents=file.read()
file.close()
#print(contents)
soup=BeautifulSoup(contents,"html.parser")
#print(soup.prettify())
#print(soup.find_all(name="a"))
#for link in soup.find_all(name="a"):
    #print(link.get("href"))
first_heading=soup.find(class_="fr1")
print(first_heading.getText())
first_heading=soup.select(selector= .fr1)