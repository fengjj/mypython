# coding: UTF-8
'''
Created on 2016年10月21日

@author: fengjj
'''
def dealLogData(filename,phone,ind):
    fileLog = open(filename)
    ofile = open('/eventapp3/2016103123/count.txt','at')
    for log in fileLog:
        cs = log.split(',')
        if int(cs[ind])>3145728:
            ofile.writelines(cs[phone]+'\t'+cs[ind]+'\n')
    ofile.close()
    fileLog.close()
if __name__ == '__main__':
    for i in range(10):
        dealLogData('/eventapp3/2016103123/flowevent_'+str(i),2,5)
        dealLogData('/eventapp3/2016103123/preflowevent_'+str(i),2,7)