from bs4 import BeautifulSoup
import requests

with open('eztv.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

match=soup.find('a')
print(match)
