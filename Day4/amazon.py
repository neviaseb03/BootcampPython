import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Adidas-Womens-Clear-Factor-Running/dp/B08TM6V7CQ/ref=sr_1_7?content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066%3Aamzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&keywords=shoes+for+women&pd_rd_r=6d0aa3b0-1e0d-4ee6-8d33-ed9fae09843c&pd_rd_w=DEt1P&pd_rd_wg=x2T9n&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=R5SZZ63KNXHT2ASAV63H&qid=1697392152&sr=8-7"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
product_title = soup.find("span", class_="a-size-large product-title-word-break").get_text().strip()
product_price = soup.find("span", class_="a-price-whole").get_text().strip()
print(f"The Price of {product_title} is Rs{product_price}")




