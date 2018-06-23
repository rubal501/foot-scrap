from scrapeador import page_get
raw_html = page_get('https://www.fifaindex.com/es-mx/player/20801/cristiano-ronaldo/')
print(len(raw_html))
