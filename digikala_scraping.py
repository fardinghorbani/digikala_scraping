from bs4 import BeautifulSoup
import requests
import json

page = requests.get("https://www.digikala.com/product/dkp-1865059")
soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
title = html.find('title')
price = html.find("meta",  attrs={'name':'twitter:data1'})
name = html.find("meta",  attrs={'property':"og:title"})
mojodi = html.find("div",  attrs={'class':"c-table-suppliers__cell c-table-suppliers__cell--conditions"})
temp =str(list(mojodi)[0])
product = json.loads(html.find("script",  attrs={'type':"application/ld+json"}).text)

print("main title : ",title.string)
print("title : ", name["content"])
print("price in toman is : ",price["content"])
print("vazeyate mojodi : ", temp[72:94])
print("name of brand : " , product["brand"]["name"])
print("average rate : " , product["aggregateRating"]["ratingValue"]," from 5")
print("last comment: ",product["review"]["description"], "  rate : ",product["review"]["reviewRating"]["ratingValue"])
print("name of author: *",product["review"]["author"],"*    data Published:",product["review"]["datePublished"] )

