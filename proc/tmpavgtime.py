#tmppre.py


import ConfigParser 
import string, os, sys, shutil
import re
import time,datetime


            
def dealFiles(paras):
    
    src_file=paras[0]
    if not os.path.exists(src_file):
        print "the file %s not exist!" % src_file
        os._exit(1)
    file_time=os.path.getctime(src_file)
    print file_time
    infile=open(src_file,'r')
    
    hour_num=0
    twohour_num=0
    num=0
    sum_time=0
    for line in infile:
        num=num+1
        rec_time=time.mktime(time.strptime(line.split(',')[33]+line.split(',')[34], '%Y%m%d%H%M%S'))
        #print rec_time
        minus_time=file_time-rec_time
        sum_time=sum_time+minus_time
        if minus_time >= 7200:
            twohour_num=twohour_num+1
        if minus_time > 3600 and minus_time < 7200:
            hour_num=hour_num+1    
    

    infile.close() 
    avg_time= sum_time/num        
    print "num=",num,"hour_num=",hour_num,"twohour_num=",twohour_num
    print "avg_time=" ,avg_time
               
def main():
    paras = [0,0,0,0,0,0,0,0]
    paras[0]=sys.argv[1]
    #paras[1]=sys.argv[2]
    print paras 

    dealFiles(paras)

  

if __name__ == '__main__':
    main()

