#import re

#handle = open('text.txt','r')
#inntt = []
#r = handle.read()
#inntt = re.findall('[0-9]+',r)
#sum =0
#for i in inntt:
#    f = int(i)
#    sum += f
    
#print sum
#---------------------------------------------------------------------------------
#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

#while True:
 #   data = mysock.recv(512)
 #   if ( len(data) < 1 ) :
  #      break
   # print data;

#mysock.close()

#---------------------------------------------------------------------------------

#import urllib
#from BeautifulSoup import *

#url = "http://python-data.dr-chuck.net/comments_366655.html"
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)

#span = soup('span')
#sum =0
#for s in span:
#    sum += int(s.contents[0])
    
#print sum
#---------------------------------------------------------------------------------
#import urllib
#from BeautifulSoup import *

#url = "http://python-data.dr-chuck.net/known_by_Neive.html"
#count = int(raw_input('Enter count- '))
#pos = int(raw_input('Enter position- '))

#for i in range(count):
#    html = urllib.urlopen(url).read()
#    soup = BeautifulSoup(html)
#    tags = soup('a')
#    l = []
#    for tag in tags:
#        l.append(tag.get('href', None))
#    url = l[pos-1]
#    print l[pos-1]

#le = len(l)    
#---------------------------------------------------------------------------------

#import urllib
#import xml.etree.ElementTree as ET

#url = "http://python-data.dr-chuck.net/comments_366656.json"
#uh = urllib.urlopen(url)
#data = uh.read()
#tree = ET.fromstring(data)
#results = tree.findall('.//count')
#sum =0
#for i in results:
#    sum += int(i.text)
#print sum
#---------------------------------------------------------------------------------
#import urllib
#import json

#url = "http://python-data.dr-chuck.net/comments_366656.json"
#uh = urllib.urlopen(url)
#r = uh.read()
#result = json.loads(r)
#comment = result['comments']
#sum =0
#for i in comment:
#    d = int(i['count'])
#    sum += d
#print sum

#---------------------------------------------------------------------------------
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        continue

    #print json.dumps(js, indent=4)

    place = js["results"][0]["place_id"]
    print place
   