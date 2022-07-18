import pdb
from bs4 import BeautifulSoup
import re
import requests
import json
import codecs

data = requests.post("http://www.pagesjaunes.ci/wp-admin/admin-ajax.php", data={
    "action": "ajax_search_tags",
    "cat_id": 3977,
    "loc_id": '',
    "list_style": "list",
    "skeyword": '',
    "lpNonce": "1c1dcb071a"
}, headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "application/x-www-form-urlencoded",

})
data = json.loads(codecs.decode(data.content, 'utf-8-sig'))
html = data.get('html')
pharma_list = []
pattern = re.compile("")
soup = BeautifulSoup(html, 'html.parser')
div = soup.find_all('div')
# <div class="clearfix lp-archive-clearfix"></div>	<div class="col-md-12  listing-style-3 list_view_v2 loop-switch-class grid_view_s4 lp-grid-box-contianer" data-title="Pharmacie Riviera M’Badon" data-postid="11369" data-lattitue="5.358187" data-longitute="-3.928399" data-posturl="http://www.pagesjaunes.ci/item/pharmacie-riviera-mbadon/">

for d in div:
    # print(re.match('http://www\.pagesjaunes\.ci/item/pharmacie-[a-zA-Z0-9\-]*/?',d.get('data-posturl') if d.get('data-posturl') is not None else ''))

    if re.match('http://www\.pagesjaunes\.ci/item/pharmacie-[a-zA-Z0-9\-]*/?',
                d.get('data-posturl') if d.get('data-posturl') is not None else ''):
        pharma = {
            'url': d.get('data-posturl'),
            'name': d.get('data-title'),
            'lat': d.get('data-lattitue'),
            'lng': d.get('data-longitute'),
        }
        location_link = d.find_all(href=re.compile("^http:\/\/www\.pagesjaunes\.ci\/location\/.*"))
        location_link = location_link[0]
        if location_link is not None:
            # pharma_list.append(a.get('href'))
            print(location_link.get('href'))
            pharma['location'] = location_link.text
        number_link = d.find_all(href=re.compile("^tel:.*"))
        number_link = number_link[0]
        location_paragraphe = d.find('p', class_='margin-bottom-0')
        if location_paragraphe is not None:
            # pharma_list.append(a.get('href'))
            print(location_paragraphe.text)
            pharma['location_full'] = location_paragraphe.text
        if number_link is not None:
            # pharma_list.append(a.get('href'))
            print(number_link.get('href'))
            pharma['number'] = number_link.text
        pharma_list.append(pharma)
print('\r\n====================================================\r\n', pharma_list,
      '\r\n==================================================\r\n')
#     # print('\r\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\r\n',d.contents[0],'\r\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\r\n')
