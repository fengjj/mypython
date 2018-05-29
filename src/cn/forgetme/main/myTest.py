# coding: UTF-8
'''
Created on 2016年10月21日

@author: fengjj
'''

if __name__ == '__main__':
    typeDict = {'12345678901':'L343','2':'L437,L438,L439,L440,L441,L442,L443,L444,L446,L447,L448,L450,L451,L344','3':'L468','4':'L469'}
    for tpye in typeDict:
        print tpye
    print '1' in typeDict
    print typeDict['2']
    print typeDict['2'].find('L4343')>-1
    import time
    x = time.localtime(1478075892)
    print x
    print time.strftime('%Y-%m-%d %H:%M:%S',x)
    #print range(1)
    print 3*1024*1024*1024