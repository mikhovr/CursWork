import urllib2
from BeautifulSoup import BeautifulSoup

def delete_dups(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
    
stopwords = open('stopwords.txt', 'w')
url = "file:///PrettyOutput.html"
soup = BeautifulSoup(urllib2.urlopen(url).read())

links = soup.findAll('table')[0].findAll('a')
linkset = set()
for link in links:
     linkset.add(str(link.contents[0]))
for item in linkset:
    stopwords.write(item+'\n')
stopwords.close()