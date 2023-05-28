import requests
from bs4 import BeautifulSoup

import pandas as pd
data = {'title':[],'price':[]}
# ,'Rating':[],'Number of reviews':[]
url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_3'
# get header from what is my header google
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

req = requests.get(url,headers=headers)

soup = BeautifulSoup(req.text,'html.parser')
# print(soup.prettify())
cards = soup.find_all('div',class_='s-result-item')
for card in cards:
    title = card.find('h2').get_text()
    print(title)
    # price = card.find('span',class_='a-price-whole').text.strip()
    # # data['title'].append(title)
    # # data['price'].append(price)
    # df = pd.DataFrame(data)
    # # df.to_csv('test/py1.csv',index=False)
    # print(df)
    # break

# print(cards)
# print(len(cards))
# print(cards[0])
# print(cards[0].find('h2').text.strip())
# print(cards[0].find('span',class_='a-price-whole').text.strip())
# print(cards[0].find('span',class_='a-icon-alt').text.strip())
# print(cards[0].find('span',class_='a-size-base').text.strip())
# print(cards[0].find('a',class_='a-link-normal a-text-normal')['href'])
# print(cards[0].find('img',class_='s-image')['src'])
# print(cards[0].find('img',class_='s-image')['alt'])
# print(cards[0].find('div',class_='a-section a-spacing-none a-spacing-top-small').text.strip())
# print(cards[0].find('div',class_='a-section a-spacing-none a-spacing-top-micro').text.strip())
# print(cards[0].find('div',class_='a-section a-spacing-none a-spacing-top-mini').text.strip())








# span = soup.select("span.a-size-medium.a-color-base.a-text-normal")
# for spans in span:
#     print(spans.string)
#     data['Product Name'].append(spans.string)

# price = soup.select("span.a-price-whole")

# for prices in price:
#     if not ("a-price.a-text-price.puis-light-weight-text" in prices.get("class") ):
#         print(prices.get_text())
#         data['Product Price'].append(prices.get_text())
#         if len(data["Product Price"]) == len(data["Product Name"]):
#             break

# rating = soup.select("span.a-icon-alt")

# for ratings in rating:
#     if not ("a-icon-alt" in ratings.get("class") ):
#         print(ratings.get_text())
#         data['Rating'].append(ratings.get_text())

# reviews = soup.select("span.a-size-base")
# for review in reviews:
#     if not ("a-size-base" in review.get("class") ):
#         print(review.get_text())
#         data['Number of reviews'].append(review.get_text())

# links = soup.select("a.a-link-normal.a-text-normal")
# for link in links:
#     if not ("a-link-normal a-text-normal" in link.get("class") ):
#         print(link.get("href"))
#         data['Product URL'].append(link.get("href"))

# df = pd.DataFrame.from_dict(data) 
# df.to_csv('test/py1.csv',index=False,encoding='utf-8')
