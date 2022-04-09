import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os.path

URL = "https://www.eseykota.com/TT/PHP_TT/TT_charts/stocks/myList.txt"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
raw = soup.prettify()
tag = (str(soup.encode_contents()))

r = re.compile('[A-Z]')
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]rn'

modSyms = []

for w in tag.split('\\n'):
    modSyms.append(w)

modSyms = list(filter(r.match, modSyms))

cleanSyms = [''.join(x for x in string if not x in special_char)
             for string in modSyms]

strong = [x for x in cleanSyms[0:15]] #make the strong list 0-14
strongDf = pd.DataFrame(strong, columns=['strong'])


weak = [x for x in cleanSyms[15:]]  #make the weak list 15-30
weakDf = pd.DataFrame(weak, columns=['weak'])



def add_days_strong(lst):
    for stock in lst:
        strongDf.loc[len(strong)] = stock
        return print (strongDf)

#
# def add_days_weak(lst):
#     for stock in lst:
#         weakDf.loc[len(weakDf)] = stock
#         return print (weakDf)

# a = add_days_strong(strong)
# b = add_days_weak(weak)

# print(strongDf)
# print(strong)
