#tmpflow.py


import ConfigParser 
import string, os, sys, shutil
import re
import time,datetime


            
def dealFiles(paras):
    
    src_dir=paras[0]
    if not os.path.exists(src_dir):
        print "the dir %s not exist!" % src_dir
        os._exit(1)
    dest_dir='/data/tmpflowdata/'
    dirlist = os.listdir(src_dir)
    mainsub_file=open('/data/windowdata/mainsub/mainsub','r')
    mainsub_dict={}
    split_num=int(paras[1])
    
    for line in mainsub_file:
        sub_phone=line.split(',')[0]
        main_phone=line.split(',')[1]
        if int(main_phone[10]) == split_num:
            mainsub_dict[sub_phone]=main_phone
    
    mainsub_file.close()
    print len(mainsub_dict)
    
    
    
    
    for file in  dirlist:
        if src_dir.endswith('/'):
            infile=open(src_dir+file,'r')
        else:
            infile=open(src_dir+os.path.sep+file,'r')
        
        outfile=open(dest_dir+file,'w')
        
        for line in infile:
            phone_no=line.split(',')[8]
            
            if mainsub_dict.has_key(phone_no):
                outfile.writelines("%s" % line)
                if int(phone_no[10]) == split_num:
                    print phone_no
                #print line
                continue
            else:
                if int(phone_no[10]) == split_num:   
                    outfile.writelines("%s" % line)
                    #print phone_no
                
        
        outfile.close()
        infile.close()          

               
def main():
    paras = [0,0,0,0,0,0,0,0]
    paras[0]=sys.argv[1]
    paras[1]=sys.argv[2]
    print paras 

    dealFiles(paras)

  

if __name__ == '__main__':
    main()


