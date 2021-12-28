# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest

car=[]
price=[]
city=[]
link=[]
fuel=[]
cv=[]
trs=[]
description=[]
num=0
while num<283:
    try:
        result=requests.get(f"https://www.*****.ma/fr/maroc/voitures/peugeot--%C3%A0_vendre?o={num}")
        
        src=result.content
        soup=BeautifulSoup(src,"lxml")
        
        cars=soup.find_all("span",{"class":"oan6tk-18 gJxgUN"})
        prices=soup.find_all("span",{"class":"sc-1x0vz2r-0 eCRZyT oan6tk-16 llzUZv"})
        cities=soup.find_all("span",{"class":"sc-1x0vz2r-0 jXlutH"})
        links=soup.find_all("a",{"class":"oan6tk-1 bPlIdR"})
        for i in range(len(cars)*2):
            city.append(cities[i].text)
            
        city=city[1::2]   
        
        for i in range(len(cars)):
            car.append(cars[i].text)
            price.append(prices[i].text)
            link.append(links[i].attrs['href'])
        num=num+1
        print("new page")
    except :
        print("stop")
        break
    
    
for i in link:
    result=requests.get(i)
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    info=soup.find_all("span",{"class":"sc-1x0vz2r-0 iZJjqC"})
    fuel.append(info[0].text)
    cv.append(info[1].text)
    trs.append(info[2].text)
    descriptions=soup.find("p",{"class":"ij98yj-0 jvMHNW"})
    description.append(descriptions.text)
      
liste=[car,price,city,fuel,cv,trs,description]
exp=zip_longest(*liste)
with open("data.csv","w",encoding="utf-8") as file:
    wr=csv.writer(file)
    wr.writerow(["voiture","prix","ville","carburant","CV","transmission","description"])
    wr.writerows(exp)