import requests
from bs4 import BeautifulSoup

uris = ['ba-journalism', 'ba-history']

for uri in uris:
    page = requests.get(f'https://www.gold.ac.uk/{uri}')

    #'Soupify' the content of the page - parse it using an HTML parser
    soup = BeautifulSoup(page.text, "html.parser")
    admin_links = soup.a['admin-login']
    print(admin_links)
