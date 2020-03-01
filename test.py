import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    title  = ''
    brand = ''
    price = ''
    features =''
    description = ''
    sub_title = ''
    img = ''
    record = []

    #Access The page
    r =  requests.get('https://www.supremenewyork.com/shop/skate/m5ihd0a2f/ex4uodg3z')
    
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')

        # IMg  
        img_sec = soup.select('figure img')
        if img_sec and img_sec[0]:
            img = 'https:'+img_sec[0]['src']
        
        #sub Titile
        sub_title_sec = soup.select('.style')
        if sub_title_sec and sub_title_sec[0]:
            sub_title = sub_title_sec[0].text.replace(',', '').strip()

        # Title 
        title_section = soup.select('h1')
        if title_section and title_section[1]:
            title = title_section[1].text

        # Description 
        description_section = soup.select('.description')
        if  description_section:
            description = description_section[0].text.replace(',', '').strip()

        #price
        price_section = soup.select('.price')
        if price_section:
            price =price_section[0].text
            price = price.replace(',', '').strip()
        
        record.append(title)
        record.append(sub_title) 
        record.append(price)
        record.append(img)
        record.append(description)

        print(title)
        print(description)
        print(price)
        print(img)
         # Store Data in CSV
        with open('result_data.csv', 'a+', encoding='utf-8') as file:
            file.write('\n')
            file.write(','.join(record))