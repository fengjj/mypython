#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
    �ļ�Ԥ����ű�
        ���߳�
        Զ��ftp��ȡ�ļ�
        �ļ��ַ������ݵ�
"""

import paramiko
import time,datetime

#��̬�����־������־�ļ�����ʱ���ܻ����ӿ���
def loginfo(*info):
    logfile = "co.log"
    output = open(logfile, 'a')
    try:
        msg = reduce(lambda x,y:str(x)+str(y),info)
        currtime = "["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]  "
        output.write(currtime+msg+"\n")
    except IOError,ex:
        print IOError,":",ex
        output.close()
        loginfo("catch:",IOError)
        exit(1)
    finally:
        output.close()

def getCo():
    try:
        t = paramiko.Transport(("132.121.86.13", 22))
        t.connect(username = "cbss_user" , password = "cBSS_2014_qsjtxfak")
        sftp = paramiko.SFTPClient.from_transport(t)
        while 1:
            time.sleep(1)
            origin_file_list = sftp.listdir("/data2/cBSS/yanmeng/gprs")
            loginfo("",len(origin_file_list))
                
                
    except Exception,ex:
        print Exception,":",ex
        t.close()
        exit(1)
    finally:
        t.close()
    
#�������
if __name__ == '__main__':
    getCo()