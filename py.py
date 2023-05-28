import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
#get html
req = requests.get(url)
htmlcontent = req.content
# print(htmlcontent)

#parse html
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)

#html tree traversal
t = soup.title
# print(type(t))

# get all para
para = soup.find_all('p')
# print(para)

# get all class inside para
# print( soup.find('p')['class'] )

# get all with class lead
# print( soup.find_all('p',class_="lead") )
# print( soup.find('p').get_text() )

# get all links
# a = soup.find_all('a')
# for link in a:
#     print(link.get('href'))

#get clickable link
# a = soup.find_all('a')
# all = set()
# for link in a:
#     if (link.get('href')!='#'):
#         linktext = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1' + link.get('href')
#         all.add(link)
#         print(linktext)

#comment
# mk ="<p><!-- comment --></p>"
# soup2 = BeautifulSoup(mk)
# print(soup2.p.string)
# exit()
#.content memory
#.children no memory

#get id content
# id = soup.find(id='id')
# print(id.contents)
# for i in id:
#     print(i)

# get string
# print(soup.find(id='id').string)

# # get parent
# print(soup.find(id='id').parent)

# # get next sibling
# print(soup.find(id='id').next_sibling)

# # get previous sibling
# print(soup.find(id='id').previous_sibling)

#css selector
# ele = soup.select('.login')
# print(ele)

#def for saving
def getdata(url,path):
    r = requests.get(url)
    with open (path,'w') as f:
        f.write(r.text)
url = ''
getdata(url,'test\index.html')

#update
c = soup.find(class_ = 'c1')
c.name = 'span'
c['class']='mclass c2class'
c.string= 'i am new'
print(c)

#new update
# ultag = soup.new_tag('ul')

# liTag = soup.new_tag('li')
# liTag.string = 'new list'
# ultag.append[liTag]

# soup.html.body.insert[0,ultag]
# with open('n.html','w') as f:
#     f.write(str(soup))

c = soup.find(class_ = 'cv')
print(c.has_attr("alt"))

# isid present
def has_class_butnot_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

result = soup.find_all(has_class_butnot_id)


import pandas as pd
data = {'title':[],'price':[]}
url = ''

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

cards = soup.find_all('div',class_='s-result-item')
for card in cards:
    title = card.find('h2').text.strip()
    price = card.find('span',class_='a-price-whole').text.strip()
    data['title'].append(title)
    data['price'].append(price)
    df = pd.DataFrame(data)
    df.to_csv('test\py.csv',index=False)
    print(df)
    break
