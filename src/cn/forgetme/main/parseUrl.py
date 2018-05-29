# -*- coding: utf-8 -*-
'''
Created on 2016年10月30日

@author: fengjj
'''
from bs4 import BeautifulSoup
import requests as rs

def do():
    data = rs.get('http://www.forgetme.cn:8080/webmarket')
    soup = BeautifulSoup(data.text,'lxml')
    print soup
    imgs = soup.select('a')
    print imgs

def do2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
        'Cookie': '_za=4ed12b83-7d81-4f86-919d-e0745d675268; _xsrf=97ca9979b4f50cd590a3d6a93d6a0304; q_c1=6d8f996fdfcb4fef8c868ae0014187f6|1477552025000|1474804813000; l_cap_id=ZDQ0MTJiYmJjMWQ5NGE2NmJkOTgzYmY1MGVlNmM1YWM=|1477729353|bf243e1e72c692146b4b43aa4a8a866bcf4c2df9; cap_id=MDJlNDAwNzI3ODczNGRlOWE4NTczZjE2NTliYjQ0NjU=|1477729353|2bc419320c333509bcc24de0d4c6c6456c79750d; d_c0=ACAAkZBhmAqPTpC-fMJYeO4wPL7KJavvpWA=|1474804815; _zap=940e3f50-4cf2-4514-aeeb-44c4b9816316; __utma=51854390.1947151648.1477730355.1477830185.1477835331.5; __utmz=51854390.1477835331.5.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; login=ODc5NDQ5OGEyN2FhNGY5ZTk5ZDBkMjJmOWZiMDUyZDc=|1477729443|ba2d7f77fcb5537f302ee8ccb24ed10c45612e83; a_t=2.0AADAGfkbAAAXAAAAS4c9WAAAwBn5GwAAACAAkZBhmAoXAAAAYQJVTaPpO1gAOuDzjHcy16QIqfaV8YlJ3gUVYCZiOzwqU-w5XHbKBp0oWezig8Miyw==; z_c0=Mi4wQUFEQUdma2JBQUFBSUFDUmtHR1lDaGNBQUFCaEFsVk5vLWs3V0FBNjRQT01kekxYcEFpcDlwWHhpVW5lQlJWZ0pn|1477835339|4386352deb2b8c8bdc54cda0bed25d3d8b49a3fb; __utmv=51854390.100-1|2=registration_date=20130618=1^3=entry_date=20130618=1; __utmb=51854390.9.5.1477835331; __utmt=1; __utmc=51854390'   
    }
    data = rs.get('https://www.zhihu.com/people/jj-feng',headers=headers)
    soup = BeautifulSoup(data.text,'lxml')
    print soup
if __name__ == '__main__':
    do2()