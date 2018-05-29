##mainsub.py

import ConfigParser 
import string, os, sys
import paramiko
import re
import time,datetime


def init(paras,cfgname):
    print cfgname
    cf = ConfigParser.ConfigParser()
    cf.read(cfgname)            
    s = cf.sections()               
    for board in cf.items('file'): 
        #print board[0]+'='+board[1] 
        if board[0] == 'mainsub_file':
            paras[0] = board[1] 
        if board[0] == 'dest_dir':
            paras[1] = board[1]                           
    print  paras[0],paras[1]

def dealfile(paras,main_dict,sub_dict,main_sub_dict):
    file_object=open(paras[0],'r')
    for line in file_object:
        group_num=line.split(',')[2]
        phone_no=line.split(',')[4]
        user_id=line.split(',')[3]
        no_type=line.split(',')[7]
        if ( phone_no[:1] == '1' ) and ( no_type == '1' ) :
            main_dict[group_num]=phone_no+','+user_id
        if ( phone_no[:1] == '1' ) and ( no_type == '2' ) :
            sub_dict[phone_no]=group_num 
    print "num of main_dict:", len(main_dict)
    print "num of sub_dict:", len(sub_dict)        
    file_object.close()
    
    outfile='%s%s' % (paras[1],"mainsub")
    output = open(outfile, 'w')
    for k in sub_dict.keys():
        group_num = sub_dict[k]      
        if  main_dict.has_key(group_num):
            main_sub_dict[k]=main_dict[group_num]  
            output.writelines("%s,%s\n" % (k,main_sub_dict[k]))
    output.close()   
    
  
           
def main(cfgname):
    paras=["",""]        
    init(paras,cfgname) 
    main_dict={}
    sub_dict={}
    main_sub_dict={}  
    
    print paras    
    dealfile(paras,main_dict,sub_dict,main_sub_dict)  
    #gen_file(paras,main_dict,sub_dict,main_sub_dict)         

if __name__ == '__main__':
    main('mainsub.cfg')


