# -*- coding:utf-8 -*-

import Queue
import re
import requests
import urllib2
from bs4 import BeautifulSoup
import base64
import sys
import datetime



def sp(url,data,lastdate):
    headers = {'content-type': 'application/json',
               'Upgrade-Insecure-Requests': '1',
               #'Cookie':'BIGipServerpool_hrssgz.gov.cn=159453356.20480.0000; BIGipServerpool_gzhr=511840428.20480.0000; GZHR_ASPNet_SessionID=d98ce8df-5744-49c4-a57a-e2782a4e33fe; _gscu_1111924005=157469504d5b2q12; _gscbrs_1111924005=1; BIGipServerpool_sydwzp_etc=2374176940.20480.0000; BIGipServerpool_gzbysrc.gzpi.cn=2223181996.20480.0000; ASP.NET_SessionId=g52hz1modcebxvm2w2drems0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

    r = requests.post(url, data=data, headers=headers)
    html = BeautifulSoup(r.text,'lxml')
    #print(html)
    for index,each in enumerate(html.select('.ListAltern td')):
        text = each.get_text()
        # print str(index)+":"+text
        # print text.encode('utf-8')
        print text[0:10]
        if("丰景军"==text):
            print data["ToPage"]+"  "+text
            return True
        elif(lastdate==text[0:10]):
            return True
def main():
    reload(sys)

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    n_days = now - delta
    print n_days.strftime('%Y-%m-%d %H:%M:%S')
    print n_days.strftime('%Y年%m月%d日')[0:18]

    sys.setdefaultencoding('utf-8')
    print "你好".encode('utf-8')
    for page in range(1,20):
        data = {'__EVENTTARGET': 'LinkButton1',
                '__EVENTARGUMENT':'',
                'ToPage':str(page),
                '__VIEWSTATEGENERATOR':'3C84D956',
                '__VIEWSTATE':'/wEPDwULLTE3MjExNTk2MzYPFgYeB1BhZ2VOdW0CAR4JUGFnZUNvdW50AmoeCFNRTFF1ZXJ5BfoBc2VsZWN0IHRvcCAxMCAqIGZyb20gKCBzZWxlY3Qgcm93X251bWJlcigpIG92ZXIgKCBvcmRlciBieSBFbmRQdWJsaWNpdHlUaW1lIGRlc2MsQnVzSUQgZGVzYykgYXMgdGVtcGlkLCogZnJvbSBCdXNpbmVzc19QZXJzb25JbnRyb2R1Y2VQdWJsaWNpdHlWaWV3IHdoZXJlIFByb2NJRCA9ICcyJyBhbmQgRW5kUHVibGljaXR5VGltZT4nMjAxOC81LzI4IDE0OjQwOjAzJyApIGFzIGEgIHdoZXJlIHRlbXBpZCBiZXR3ZWVuIHswfSBhbmQgezF9IBYCAgEPZBYIAgEPPCsACwEADxYIHghEYXRhS2V5cxYKBSBmMWU1NzVlODkzZTk0ODcyYjU1ODI4MWRmOTNlODc0ZAUgMGM4MDNlNDVlYmZlNGRkYThjOTgyNThhYWQzMWMzNzAFIDdkYTRlOTZiZWQ0NjQ2YTg5MGQ5OTczZmRjZDIxMzJjBSA3MmQ5ZTJmMTgyMDk0ZmJhODIxZTkyMzAyOGZmMjQyNwUgZmVhYzgzMzE4OGUxNGVjMGIyYjYzMjViNDM0ZDY1YmUFIGYxZGY0ZTA1YTVhMzQ4YWFiMjRmYjIyOTczNWU3OWU5BSBlOGFjZTRjN2U0MDY0MjUyOTVhY2MyZmI5NzUwM2VkNwUgZDYwYTc3Y2UyMDhhNDQ4NDlkMzFmYTAyMTY2NzQwOTQFIGNkOWJiMjgzNjRkNzQxODFhOTRmMjU2MjAwZWVhYjM2BSBiMzE1ODE4ZWI3ODY0M2UxYjk1MzVhYTQ0ZjUwNjlmMx4LXyFJdGVtQ291bnQCCh8BAgEeFV8hRGF0YVNvdXJjZUl0ZW1Db3VudAIKZBYCZg9kFhQCAQ9kFgxmDw8WAh4EVGV4dAUJ6LCi6YeR5ZCNZGQCAQ8PFgIfBgUq5bm/5bee5biC5rW354+g5Yy65rCR5pS/5bGA5ama5ae755m76K6w5aSEZGQCAg8PFgIfBgUG5ZCM5oSPZGQCAw8PFgIfBgUw5bm/5bee5biC5rW354+g5Yy65Lq65Yqb6LWE5rqQ5ZKM56S+5Lya5L+d6Zqc5bGAZGQCBA8PFgIf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'
                }
        #data={'some':''}
        print "加载当前页："+str(page)+"... ..."
        flag = sp('http://www.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/PersonIntroducePublicity.aspx',data,n_days.strftime('%Y年%m月%d日'))
        if flag:
            break
    print "处理完毕"
main()

