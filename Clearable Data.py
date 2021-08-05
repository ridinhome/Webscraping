import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://www.lch.com/services/swapclear/what-we-clear'
req = requests.get(url)
dictionary = {"Product":[],"Clearables":[]}

soup = BeautifulSoup(req.content,"lxml")
data = soup.find_all('table')

def return_list(clearables):
    clearables_list=[]
    for item in clearables:
        clearables_list.append(item.string)
    return (clearables_list)

for item in data:
    dictionary['Product'].append(item.find("strong").text)
    if len(item.find('td').string) < 3:
        clearables = item.find_all('td')[4:]
    else:
        clearables = item.find_all('td')
    dictionary['Clearables'].append(return_list(clearables))


# print (dictionary)

df = pd.DataFrame(dictionary)
df = df[df['Product'] != 'IRS']
df['Product'] = df['Product'].str.split("/")
df = df.explode(column='Clearables')
df = df.explode(column='Product')
print(df)
#






