import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

if __name__ == '__main__':

    title  = ''
    brand = ''
    price = ''
    features =''
    description = ''
    img = ''
    record = []

    with open('links.txt',encoding='utf-8') as f:
        lines = f.readlines()
        for link in lines:

            #Access The page
            r =  requests.get(link.replace('\n', '').strip(), headers=headers, timeout=5)
            
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
                # Store Data in CSV
                with open('result_data.csv', 'a+', encoding='utf-8') as file:
                    file.write('\n')
                    file.write(','.join(record))
                record = []