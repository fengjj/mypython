#! /usr/bin/python
#-*- coding: utf-8 -*-

try:
    import configparser
except:
    from six.moves import configparser
import string, os, sys, shutil
#import paramiko
import re
import time,datetime


def getCfg():
    print(sys.argv)
    cfgfile = 'getdata.cfg'
    cfg_dict = {}
    cf = ConfigParser.ConfigParser()
    cf.read(cfgfile)
    if sys.argv[1] != None:
        for kv in cf.items(sys.argv[1]):
            cfg_dict[kv[0]] = kv[1]
        
        print(cfg_dict)
        return cfg_dict
    else:
        print ("\nargv is invalid! please check your input arg and restart python!!!")
        exit(1)
    
def getFile():
    cfg_dict = getCfg()
    loginfo("start_copy_",sys.argv[1],"data...")
    if sys.argv[1] == "pre" or sys.argv[1] == "after":
        while True:
            time.sleep(1)
            file_list = []
            origin_file_list = os.listdir(cfg_dict['origin_dir'])
            if len(origin_file_list) > 0:
                last_month = (datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)).strftime('%Y%m')
                for fname in origin_file_list:
                    origin_file = os.path.join(cfg_dict['origin_dir'],fname)
                    if os.path.isdir(origin_file):
                        #print "d_",origin_file,"_d"
                        continue
                    if last_month in fname:
                        os.remove(origin_file)
                        loginfo("last month origin_file is deleted:",fname)
                        continue
                    if fname.startswith(cfg_dict['file_prefix']):
                        file_list.append(fname)
                    if sys.argv[1] == "pre":
                        if fname.startswith(cfg_dict['order_prefix']) and fname.find(cfg_dict['order_instr']) > -1:
                            order_file = os.path.join(cfg_dict['order_dir'],fname)
                            shutil.copy(origin_file,order_file)
                            if cfg_dict['get_way'] == "mv":
                                os.remove(origin_file)

                doCopy(cfg_dict,file_list)

    elif sys.argv[1] == "dpi" or sys.argv[1] == "sig":
        t = paramiko.Transport(cfg_dict['ip_addr'], int(cfg_dict['port']))
        t.connect(username = cfg_dict['username'] , password = cfg_dict['password'])
        sftp = paramiko.SFTPClient.from_transport(t)
        try:
            while True:
                time.sleep(1)
                dirlist = sftp.listdir(cfg_dict['origin_dir'])
                dirlist.sort()
                if len(dirlist) > 0:
                    for fname in dirlist:
                        origin_file = os.path.join(cfg_dict['origin_dir'],fname)
                        if sys.argv[1] == "sig":
                            last_file = cfg_dict['last_file']
                            if fname.startswith(cfg_dict['file_prefix']) and fname.endswith(cfg_dict['file_suffix']) and fname > last_file:
                                last_file = fname
                                origin_file = os.path.join(cfg_dict['origin_dir'],fname)
                                locale_file = os.path.join(cfg_dict['local_dir'],fname)
                                split_file = os.path.join(cfg_dict['split_dir'],fname)
                                sftp.get(origin_file, locale_file)
                                loginfo("get_file:",fname)
                                if cfg_dict['get_way'] == "mv":
                                    sftp.remove(origin_file)
                                
                                real_file = os.path.join(cfg_dict['local_dir'],fname)
                                split_cmd = 'split -l %s %s %s.SPLIT.' % (cfg_dict['split_size'],real_file,split_file)
                                os.popen(split_cmd)
                                if cfg_dict['get_way'] == "mv":
                                    os.remove(real_file)
                        elif sys.argv[1] == "dpi":
                            if fname.startswith(cfg_dict['file_prefix']) and fname.endswith(cfg_dict['file_suffix']):
                                day = datetime.datetime.now().strftime('%Y%m%d')
                                backup_dir = os.path.join(cfg_dict['local_dir'],day)
                                if not os.path.exists(backup_dir):
                                    os.mkdir(backup_dir)
                                    
                                origin_file = os.path.join(cfg_dict['origin_dir'],fname)
                                locale_file= os.path.join(cfg_dict['local_dir'],fname)
                                backup_file = os.path.join(backup_dir,fname)
                                sftp.get(origin_file, backup_file)
                                shutil.copy(backup_file, locale_file)
                                if cfg_dict['get_way'] == "mv":
                                   sftp.remove(origin_file)
                            
        except(IOError,UnboundLocalError):
            t.close()
            loginfo("IOError,UnboundLocalError,python stopped")
            exit(-1)
        t.close()
        
        
def doCopy(cfg_dict,file_list):
    if len(file_list) > 0:
        minute = datetime.datetime.now().strftime('%M')
        dest_len = len(os.listdir(cfg_dict['dest_dir']))
        max_file = int(cfg_dict['max_file'])
        while minute >= cfg_dict['minute']:
            loginfo("getdata.py is started but not copy file while minute >=",cfg_dict['minute'])
            time.sleep(6)
            minute = datetime.datetime.now().strftime('%M')
            
        while dest_len >= max_file:
            loginfo("the dest_dir files is gt_",max_file,",_dest_len:",dest_len)
            time.sleep(6)
            dest_len = len(os.listdir(cfg_dict['dest_dir']))
        
        hour = datetime.datetime.now().strftime('%Y%m%d%H')
        backup_dir = os.path.join(cfg_dict['backup_dir'],hour)
        if not os.path.exists(backup_dir):
            os.mkdir(backup_dir)
        
        if len(file_list) > max_file:
            fetch_num = max_file
        else:
            fetch_num = len(file_list)
            
        if cfg_dict['time_sort'].lower() == "true":
            file_dict = {}
            sorted_list = []
            for fname in file_list:
                origin_file = os.path.join(cfg_dict['origin_dir'],fname)
                if os.path.isfile(origin_file):
                    #mt = time.localtime(os.path.getmtime(origin_file))
                    ct = time.localtime(os.path.getctime(origin_file))
                    file_dict[fname] = ct
                    #print "mtime:",time.strftime('%H:%M:%S',mt),"ctime:",time.strftime('%H:%M:%S',ct),"==",fname
            for fd in sorted(file_dict.items(),key=lambda x:x[1]):
                loginfo("ctime:",time.strftime('%H:%M:%S',fd[1]),"==",fd[0])
                sorted_list.append(fd[0])
            file_list = sorted_list
        
        for fname in file_list[:fetch_num]:
            origin_file = os.path.join(cfg_dict['origin_dir'],fname)
            #print "ctime:",os.path.getctime(origin_file),"  cp_origin_file",origin_file
            dest_file = os.path.join(cfg_dict['dest_dir'],fname)
            backup_file = os.path.join(backup_dir,fname)
            shutil.copy(origin_file,backup_file)
            shutil.copy(origin_file,dest_file)
            if cfg_dict['get_way'] == "mv":
                os.remove(origin_file)
                
        loginfo("copy_",fetch_num,"_flow_files")
        del file_list[:fetch_num]

    
def loginfo(*info):
    logfile = sys.argv[1]+".log"
    output = open(logfile, 'a')
    try:
        msg = reduce(lambda x,y:str(x)+str(y),info)
        currtime = "["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]  "
        output.write(currtime+msg+"\n")
    except(IOError):
        output.close()
    finally:
        output.close()

def main():
    dic = getCfg()
    


if __name__ == '__main__':
    main()
