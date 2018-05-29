# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日

@author: fengjj
'''
import time
import sys
def dealLogData(custdict,typeDict,filename):
    fileDict={}
    result = {}
    for type in range(1,5):
        type = str(type)
        result[type]={}
        ps = typeDict[type]
        print 'start:','type',type,'ps:',ps
        fileLog = open(filename)
        for log in fileLog:
            cs = log.split(',') #5L;7P
            if len(cs)<10:
                continue
            else:
                if ps.find(cs[5])>-1:
                    print 'type',type,' ',cs[5],'in', cs[7]
                    #print cs[7]
                    if cs[7] in custdict:
                        del custdict[cs[7]]
                        result[type][cs[7]+'\t'+time.localtime(int(cs[9]))]=''
        fileLog.close()
    return result
if __name__ == '__main__':
    d=''
    if len(sys.argv)>1:
        d= '.'+sys.argv[1]
    fileObj = open('/data/websale/cust_groups/201610119')
    custdict = {}
    result = {}
    for line in fileObj:
        custdict[line[:11]]=''
    fileObj.close()
    print len(custdict)
    typeDict = {'1':'L343','2':'L437,L438,L439,L440,L441,L442,L443,L444,L446,L447,L448,L450,L451,L344','3':'L468','4':'L469'}
    for i in range(10):
        filename = '/data/eventapp4/locationevent/log/SubscriberFromEspToKafka_DpiUserClassTargetData'+str(i)+'.console'+d
        result = dealLogData(custdict,typeDict,filename)
        
        for type in typeDict:
            ofile = open('/data/eventapp4/count/cou_'+type,'at')
            print type,len(result[type])
            for r in result[type]:
                ofile.writelines(r+'\n')
            ofile.close()
        print len(custdict)
    ofile = open('/data/eventapp4/count/cou_other','wt')
    for r in custdict:
        ofile.writelines(r+'\n')
    ofile.close()