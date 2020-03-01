import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    total_products_page_links = []
    #Access The page
    r =  requests.get('https://www.supremenewyork.com/shop/all')
    
    if r.status_code == 200:    
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        list_all_links = soup.select('.inner-article a')
        for l in list_all_links:
            total_products_page_links.append('https://www.supremenewyork.com'+l['href'])

        with open('links.txt', 'a+', encoding='utf-8') as file:
            file.write('\n'.join(total_products_page_links))
            #Access detail page
            # response =  requests.get('https://www.supremenewyork.com'+link)
            # detail_html = response.text
            # detail_soup = BeautifulSoup(detail_html, 'lxml')


 