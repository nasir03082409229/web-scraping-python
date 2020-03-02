import requests
from bs4 import BeautifulSoup

img_urls = []

r =  requests.get('https://www.supremenewyork.com/shop/jackets/ykpf4b5m1/ke6bj79r8')
if r.status_code == 200:  
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    parent = soup.find('a', {'class' :'selected'})
    parent = parent.find_parent()
    parent = parent.select('img')
    for i in parent:
        img_urls.append('https:'+i['src'].replace('sw','ma'))
    print(img_urls)
    