from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp').content #requita informação ao site
soup = BeautifulSoup(site, 'html.parser')# traz o html do site

# print(soup.prettify()) #imprime e tranforma em string

# temperatura = soup.find('span', 'class_="-gray-light" id="min-temp-1"')
# print(temperatura)

print(soup.title.string)