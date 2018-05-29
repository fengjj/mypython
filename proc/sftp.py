import ConfigParser 
import string, os, sys
import paramiko
import re
import time,datetime


def init(paras,sftpname):
    cf = ConfigParser.ConfigParser()
    cf.read(sftpname)            
    s = cf.sections()               
    #print 'section:', s  
    for board in cf.items('downloadcfg'): 
        #print board[0]+'='+board[1] 
        if board[0] == 'ip_addr':
            paras[0] = board[1] 
        if board[0] == 'port':
            paras[1]=board[1]  
        if board[0] == 'username':
            paras[2]=board[1]  
        if board[0] == 'password':
            paras[3]=board[1]
        if board[0] == 'remote_dir':
            paras[4]=board[1]
        if board[0] == 'local_dir':
            paras[5]=board[1]              
    #print  ip_addr,port,username,password,remote_dir,local_dir
    
    cf1 =  ConfigParser.ConfigParser()
    cf1.read('fetch.cfg')
    s1=  cf1.sections()  
    print 'section:', s1
    for board1 in cf1.items('lastfetch'):
        print board1[0],board1[1]
        if board1[0] == 'file_name':
            paras[6] = board1[1]
        if board1[0] == 'fetch_time':
            paras[7] = board1[1] 
     
    #print paras
    
def getFiles(paras,file_list,endfile): 
    
    del file_list[:]
    print "file_list: " ,file_list
    t = paramiko.Transport((paras[0], int(paras[1])))
    t.connect(username = paras[2] , password = paras[3] ) 
    sftp = paramiko.SFTPClient.from_transport(t) 
    dirlist = sftp.listdir(paras[4])  
    #print "Dirlist:", dirlist 
    last_file=paras[6]
    print last_file,paras[6]
    last_file_time=last_file.split('_')[2].split('.')[0]
    print last_file_time
    for file in dirlist:
        if file.endswith('.DAT'):
            #print file
            file_time=file.split('_')[2].split('.')[0]
            #print cmp(last_file_time,file_time),file
            if cmp(last_file_time,file_time) < 0:
               file_list.append(file)
               if cmp(endfile[0],file) < 0:
                   endfile[0] = file
               
    print  "need to sftp file list: " , file_list 
    print  "max file: "  , endfile[0]       
    t.close()           
            
            
        
        
    
def sftpandsplit(paras,file_list):

    t = paramiko.Transport((paras[0], int(paras[1])))
    t.connect(username = paras[2] , password = paras[3] ) 
    sftp = paramiko.SFTPClient.from_transport(t)
    for file in  file_list:
        remote_file='%s/%s' % (paras[4],file)
        locale_file='%s/%s' % (paras[5],file)
        sftp.get(remote_file, locale_file)
    #file_list =  []
    t.close() 
    
    data_dir='%s' % paras[5]
    os.chdir(data_dir)
    output=os.popen('pwd')
    print output.read()
    
    for file in  file_list:
        split_cmd='split -l 100000 %s %s.SPLIT.' % (file,file)
        print 'split_cmd=',split_cmd
        os.popen(split_cmd)
        move_cmd='mv %s.SPLIT.* %s/SPLIT/' % (file,paras[5])
        os.popen(move_cmd)
        os.remove(file)
    

def updateFile(paras,endfile,ori_dir):
    paras[6] = endfile[0]
    curr_time=time.strftime('%Y%m%d%H%M%S')
    print curr_time
    os.chdir(ori_dir[0])
    file_object = open('fetch.cfg','w')
    file_object.write('[lastfetch]\n')
    file_object.write('file_name=%s\n'%endfile[0])
    file_object.write('fetch_time=%s\n'%curr_time)
        
        
   
               
def main(sftpname):
    paras = [0,0,0,0,0,0,0,0]
    endfile = [] 
    file_list = []  
    ori_dir = [0]        
    init(paras,sftpname)
    print paras 
    endfile.append(paras[6])
    
    output = os.popen('pwd')
    ori_dir[0] = output.read().rstrip()
    while True:
        curr_time=time.strftime('%Y%m%d %H:%M:%S')
        print "getFiles start:", curr_time
        getFiles(paras,file_list,endfile)
        curr_time=time.strftime('%Y%m%d %H:%M:%S')
        print "getFiles end,start to sftpSrv curr_time=%s,file_list=%s" %(curr_time,file_list)
        sftpandsplit(paras,file_list)
        curr_time=time.strftime('%Y%m%d %H:%M:%S')
        print "sftpSrv end,start to updateFile ", curr_time 
        updateFile(paras,endfile,ori_dir)  
        curr_time=time.strftime('%Y%m%d %H:%M:%S')
        print "updateFile end, sleep some seconds ", curr_time 
        #time.sleep(5)
        
    

if __name__ == '__main__':
    main('sftp.cfg')


