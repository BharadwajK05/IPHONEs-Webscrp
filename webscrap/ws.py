import requests
import numpy 
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='KzDlHZ')
# print(names)
name=[]
for i in names[0:15]:
    d=i.get_text()
    name.append(d)
# print(name)
prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[0:15]:
    d=i.get_text()
    price.append(d)
# print(price)
ratings=soup.find_all('div',class_='XQDdHH')
rate=[]
for i in ratings[0:15]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)
reviews=soup.find_all('span',class_='Wphh3N')
review=[]
for i in reviews[0:15]:
    d=i.get_text()
    review.append(d)
#print(review)
features=soup.find_all('div',class_='_6NESgJ')
Feature=[]
for i in features[0:15]:
    d=i.get_text()
    Feature.append(d)
# print(Feature)
links=soup.find_all('a',class_='CGtC98')
Link=[]
for i in links[0:15]:
    d="https://www.flipkart.com"+i['href']
    Link.append(d)
# print(Link)
images=soup.find_all('img',class_='DByuf4')
Image=[]
for i in images[0:15]:
    d=i['src']
    Image.append(d)
#print(Image)
data={'names':name,
      'prices':price,
      'ratings':rate,
      'reviews':review,
      'features':Feature,
      'links':Link,
      'images':Image
}
df=pandas.DataFrame(data)
#print(df)
df.to_csv("Iphones.csv")



