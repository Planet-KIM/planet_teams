from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np

html = urlopen('http://elwlsek.tistory.com/1586')
bs = BeautifulSoup(html, 'html.parser')

arrayA = []
for item in bs.find_all('p', {'align':'center'}):

    arrayA.append(item.get_text())
    if len(arrayA))%4==2: