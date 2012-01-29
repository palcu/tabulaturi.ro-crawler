from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from operator import attrgetter

link = 'http://www.tabulaturi.ro/acorduri.php?tab_id='
f = open('songs.txt', 'a')
v = []

class Song:
	def __init__(self, artist, song, stars, persons):
		self.artist, self.song, self.stars, self.persons = artist, song, stars, persons
		self.id = 0
		self.link = ""

def parsePage(page):
	page = urlopen(page)
	# page = html.decode('utf-8')
	soup = BeautifulSoup(page)

	
	persons = soup.find('td', { "class" : "tabinfo2"})
	if hasattr(persons, 'contents'):
		persons = persons.contents[0].split(' ')[0]
	else:
		return False
	# print persons

	artistsong = soup.find('td', { "class" : "tabtitle"})

	song = artistsong.contents[2][3:].strip()
	# print song

	artist = artistsong.a.contents[0]
	# print artist

	stars = soup.findAll('img', src="images/star_full.png")
	# print len(stars)

	return Song(artist, song, len(stars), persons)

for i in range(5000,7611):
	myLink = link + str(i)
	# print myLink
	song = parsePage(myLink) 
	# s = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n\n'.format(song.id, song.link, song.artist.encode('utf-8'), song.song.encode('utf-8'), song.stars, song.persons)
	if song != False:
		song.id = i
		song.link = myLink
		#v.append(song)
		print '{0} {1}'.format(i, song.song.encode('utf-8'))
		# f.write('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n\n'.format(song.id, song.link, song.artist.encode('utf-8'), song.song.encode('utf-8'), song.stars, song.persons))
	else:
		print '{0} False'.format(i)


# v.sort(key=attrgetter('stars', 'persons'), reverse=True)

#for i in v:
	#f.write('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n\n'.format(i.id, i.link, i.artist.encode('utf-8'), i.song.encode('utf-8'), i.stars, i.persons))
