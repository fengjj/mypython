import Queue
import re
import requests
import urllib2
from bs4 import BeautifulSoup
import base64

def sp(url):

    data = {'some': '0'}
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    r = requests.get(url, data=data, headers=headers)
    html = BeautifulSoup(r.text,'lxml')
    print(html)
    for index,each in enumerate(html.select('#comments span.img-hash')):
        with open('{}.jpg'.format(index),'wb') as jpg:
            u = each.get_text()
            u = "http:"+base64.b64decode(u)
            print str(index)+":"+u
            try:
                src = requests.get(u,data=data, headers=headers,stream=True).content
                jpg.write(src)
            except IOError:
                print("url:" + u)

sp('http://jandan.net/ooxx/page-50689337#comments')

