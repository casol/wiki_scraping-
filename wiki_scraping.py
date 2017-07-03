from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import csv


html = urlopen("https://en.wikipedia.org/wiki/List_of_museum_ships")
bs_obj = BeautifulSoup(html, "html.parser")

table = bs_obj.findAll("table", {"class": "wikitable"})[0]
rows = []
# easy solution best solution ?
for row in table.findAll("tr"):
    rows.append(row)

print(rows[529])
    #for link in t.findAll("a", href=re.compile("^(/wiki/)")):
        #if 'href' in link.attrs:
            #print(link.attrs['href'])


"""

csv_file = open('/home/christopher/Desktop/wiki_scraping/table.csv', 'wt')
writer = csv.writer(csv_file)

try:
    for row in rows:
        csv_row = []
        for cell in row.findAll(['td']):
            csv_row.append(cell.get_text())
            writer.writerow(csv_row)
finally:
    csv_file.close()
"""