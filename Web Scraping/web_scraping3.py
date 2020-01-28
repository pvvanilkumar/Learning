#get latest version of python from python.org

import requests
from bs4 import BeautifulSoup

 
URL = "https://www.python.org/downloads/"
print("Getting data from the URL")
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
buttons = soup.find('p', attrs = {'class':'download-buttons'})

versions = buttons.findAll('a')
text =versions[0].text
print(text.split()[-1])

