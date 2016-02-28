import requests, bs4

res = requests.get('http://www.billboard.com/charts/hot-100')
res.raise_for_status()
bilbSite = bs4.BeautifulSoup(res.text, "html.parser")

bilbFile = open('bilboard10.html', 'w')
bilbFile.write(str(bilbSite))
bilbFile.close()

bilbFile = open('bilboard10.html')
bilbSoup = bs4.BeautifulSoup(bilbFile.read(), "html.parser")

top100songs = bilbSoup.select('div.chart-row__title h2')
top100artist = bilbSoup.select('div.chart-row__title h3')

bilbFile.close()

top10songs = []
top10artists = []
top10artists2 = []

for i in range(0,10): 
	top10songs.append(top100songs[i].getText())
	top10artists.append(top100artist[i].getText().rsplit())

for i in top10artists:
	art = " ".join(i)
	top10artists2.append(art)

for music,artist in zip(top10songs, top10artists2):
	print(str(top10songs.index(music)+1) +  ". " + music + " - " + artist)