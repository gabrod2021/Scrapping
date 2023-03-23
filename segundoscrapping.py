from bs4 import BeautifulSoup
import requests

website = 'https://es.wikipedia.org/wiki/Portal:Software_libre' 
result=requests.get(website)
content=result.text

soup=BeautifulSoup(content, 'lxml')
#print(soup.prettify())


title = soup.find('b').get_text()


transcript = soup.find('div', class_='portal-column-left-60').get_text()
#print(title)
#print(transcript)

with open(f'{title}.txt', 'w',encoding="utf-8") as file:
    file.write(transcript)