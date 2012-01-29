from operator import attrgetter

class Song:
        def __init__(self, id, link, artist, song, stars, persons):
                self.id, self.link, self.artist, self.song, self.stars, self.persons = id, link, artist, song, stars, persons

f = open('songs.txt', 'r')
g = open('ranking.txt', 'w')

songs = []
v = f.readlines()
for i in range(0,len(v)-1,7):
	# print '{0} - {1}'.format(v[i+2].strip(),v[i+3].strip())
	if v[i+5].strip().find('.') == -1:
		songs.append(Song(v[i].strip(), v[i+1].strip(), v[i+2].strip(), v[i+3].strip(), int(v[i+4].strip()), int(v[i+5].strip())))

songs.sort(key=attrgetter('persons', 'stars'), reverse=True)

for i in songs:
        g.write('{2} - {3} | {4}* {5} persoane => {1}\n'.format(i.id, i.link, i.artist, i.song, i.stars, i.persons))
