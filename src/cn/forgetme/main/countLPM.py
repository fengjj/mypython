# -*- coding: utf-8 -*-
'''
Created on 2016年11月19日
统计场景触发量，按照每分钟
@author: fengjj
'''
import sys
import commands


def getCouPS(d,l ):
    couDict = {} #每秒触发多少条
    for i in range(10):
        filename = '/data/eventapp4/locationevent/log/SubscriberFromEspToKafka_DpiUserClassTargetData'+str(i)+'.console'+d
        fileLog = open(filename)
        for log in fileLog:
            log
    return couDict
if __name__ == '__main__':
    d='' #日期
    l=sys.argv[1] #指标值
    if len(sys.argv)>2:
        d= '.'+sys.argv[2]
    coudic = getCouPS(d,l)
    