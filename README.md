# [tabulaturi.ro](http://tabulaturi.ro) crawler

Tabulaturi is a well known Romanian website with guitar tabs for songs. But it misses a feature: a ranking with the best tabs.

So I wrote a [`crawler`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/crawler.py) in Python, that uses `urllib2` and `BeautifulSoup`, parses each page with tabs, and then writes the needed information to [`songs.txt`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/songs.txt).

Then [`parser.py`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/parser.py), takes that file and sorts the songs by the number of persons who voted, then by the number of stars, and outputs everything to [`ranking.txt`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/ranking.txt).
