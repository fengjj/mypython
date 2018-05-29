# -*- coding: utf-8 -*-
'''
Created on 2016年10月27日

@author: fengjj
'''
#import ConfigParser
import sys
'''
def getCfg(configName):
    cfg_dict = {}
    cf = ConfigParser.ConfigParser()
    cf.read(configName)
    for kv in cf.items(sys.argv[1]):
        cfg_dict[kv[0]] = kv[1]
    return cfg_dict
'''
def split(dirDic,custid):
    fileObj = open('C:\\Users\\fengjj\\Desktop\\'+custid+'\\'+custid)
    output = {}
    tmp={}
    for i in range(0,10):
        output[i] = open('C:\\Users\\fengjj\\Desktop\\'+custid+'\\'+custid+'_'+str(i),'wt')
    for line in fileObj:
        if line not in tmp:
            print(line[:11])
            tmp[line]=''
            output[int(line[10])].writelines(custid+','+line[:11]+',0\n')
    for i in range(0,10):
        output[i].close()
    fileObj.close()
if __name__ == '__main__':
    #dirDic = getCfg('cust.cfg')
    #split('',sys.argv[1])
    #201610119
    split('','201611151')