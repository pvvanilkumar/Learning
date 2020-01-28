#webscraping


import requests
from bs4 import BeautifulSoup
 
URL = "https://www.passiton.com/inspirational-quotes"
print("Getting data from the url")
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes = soup.find('div', attrs = {'id':'all_quotes'})

out=open("inspirational-quotes.txt", "w")
 
for quotecount,row in enumerate(quotes.findAll('img')):
	quote=row.get("alt")
	quote = quote.split(".")[0]
	print("Writing quote ", quotecount + 1)
	out.write(quote + "\n")
out.close()
		
		
		
#code based on https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
