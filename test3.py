from bs4 import BeautifulSoup
from scrapeador import page_get

raw_html = page_get('https://www.fifaindex.com/es-mx/player/20801/cristiano-ronaldo/')

html = BeautifulSoup(raw_html, 'html.parser')
a=True;
for span in html.select('span'):
   if span['class'] == ['label', 'rating', 'r5']:
        print(span.text)
