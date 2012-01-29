# [tabulaturi.ro](http://tabulaturi.ro) crawler

Tabulaturi is a well known Romanian website with guitar tabs for songs. But it misses a feature: a ranking with the best tabs.

So I wrote a [`crawler`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/crawler.py) in Python, that uses `urllib2` and `BeautifulSoup`, parses each page with tabs, and then writes the needed information to [`songs.txt`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/songs.txt).

Then [`parser.py`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/parser.py), takes that file and sorts the songs by the number of persons who voted, then by the number of stars, and outputs everything to [`ranking.txt`](https://github.com/palcu/tabulaturi.ro-crawler/blob/master/ranking.txt).

### License
Copyright (C) 2012 Alexandru Palcuie

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
