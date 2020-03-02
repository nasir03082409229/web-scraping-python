import urllib.request
import os
from pathlib import Path

dirName = 'category/product_name/color/'
# Path(dirName).mkdir(parents=True, exist_ok=True)
# if not os.path.exists(dirName):
# try:
#     # Create target Directory
#     os.mkdir(dirName)
#     print("Directory " , dirName ,  " Created ") 
# except FileExistsError:
#     print("Directory " , dirName ,  " already exists")

os.makedirs(dirName, exist_ok=True)
url = 'https://assets.supremenewyork.com/184829/ma/UdOuR0JdzFg.jpg'
file_path = dirName
urllib.request.urlretrieve(url,file_path+ 'file_name0'+'.jpg')

 