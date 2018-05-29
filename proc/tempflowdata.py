
import ConfigParser 
import string, os, sys, shutil
import re
import time,datetime


def init(paras,cfgname):
    cf = ConfigParser.ConfigParser()
    cf.read(cfgname)            
    s = cf.sections()               
    #print 'section:', s  
    for board in cf.items('afterpaycfg'): 
        #print board[0]+'='+board[1] 
        if board[0] == 'src_dir':
            paras[0] = board[1] 
        if board[0] == 'dest_dir':
            paras[1]=board[1]  
        if board[0] == 'backup_dir':
            paras[2]=board[1]  
        if board[0] == 'file_prefix':
            paras[3]=board[1]
                        
    #print  paras[0],paras[1],paras[2],paras[3]
    #print paras
    
def getFiles(paras,sorted_list): 
    file_dict = {}
    file_dict_list = []
    src_dir=paras[0]
    file_prefix=paras[3]
    os.chdir(src_dir)
    dirlist = os.listdir(src_dir) 
    last_month=(datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)).strftime('%Y%m')
    for file in  dirlist:
        if os.path.isdir(file):
            continue
            
        if not file.startswith(file_prefix) and os.path.isfile(file):
            os.remove(file)
            continue

        if last_month in file:
            os.remove(file)
            print "last month file is deleted:%s" % file
            continue
            
        if  file.startswith(file_prefix) and os.path.isfile(file):
            ctime = os.path.getctime(file) 
            #print ctime
            file_dict[file]=ctime
            
    print  "length of file_dict:%s" % len(file_dict) 
    file_dict_list=sorted(file_dict.items(),key=lambda x:x[1])
    for file in  file_dict_list:
        sorted_list.append(file[0])
    print "length of sorted_list:%s" % len(sorted_list)
    #print sorted_list[:5]
            
def dealFiles(paras,sorted_list):
    src_dir=paras[0]
    dest_dir=paras[1]
    back_dir=paras[2]
    while len(sorted_list) > 0:
            
        hour=datetime.datetime.now().strftime('%Y%m%d%H')
        back_dir_name='%s%s' % (back_dir,hour)
                
        if len(sorted_list) > 100:
            fetch_num=100
        else:
            fetch_num=len(sorted_list)
        
        print  "fetch_num=",fetch_num   
                
        for file in sorted_list[:fetch_num]:
            src_file=src_dir+file
            dest_file=dest_dir+file
            back_file=back_dir_name+os.path.sep+file
            #shutil.copy(src_file,back_file)
            #shutil.copy(src_file,dest_file)
            os.remove(file)
            
        del sorted_list[:fetch_num]
                     
 
               
def main(cfgname):
    paras = [0,0,0,0,0,0,0,0]
    file_list = [] 
    sorted_list = []
    ori_dir = [0]        
    init(paras,cfgname)
    print paras 
    getFiles(paras,sorted_list)
    dealFiles(paras,sorted_list)
    
    #while True:
    #    curr_time=time.strftime('%Y%m%d %H:%M:%S')
    #    print "getFiles start:", curr_time
    #    getFiles(paras,file_list,endfile)
    #    curr_time=time.strftime('%Y%m%d %H:%M:%S')
    #    print "getFiles end,start to sftpSrv curr_time=%s,file_list=%s" %(curr_time,file_list)
    #    sftpandsplit(paras,file_list)
    #    curr_time=time.strftime('%Y%m%d %H:%M:%S')
    #    print "sftpSrv end,start to updateFile ", curr_time 
    #    updateFile(paras,endfile,ori_dir)  
    #    curr_time=time.strftime('%Y%m%d %H:%M:%S')
    #    print "updateFile end, sleep some seconds ", curr_time 
    #    time.sleep(10)
        
    

if __name__ == '__main__':
    main('config.cfg')


