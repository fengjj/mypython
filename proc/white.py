##white_deal.py

import ConfigParser 
import string, os, sys
import paramiko
import re
import time,datetime



def dealfile(paras,white_dict):
    file_object=open(paras[0],'r')
    for line in file_object:
        white_dict[line]=line
    print "num of white_dict:", len(white_dict)        
    file_object.close()
    
    file_object=open(paras[1],'r')
    for line in file_object:
        if white_dict.has_key(line):
            print line
            del white_dict[line]        
    file_object.close()
    
    output = open("deal_white.list", 'w')
    for k in white_dict.keys(): 
        output.writelines("%s" % k)
    output.close() 
    
    print "end num of white_dict:", len(white_dict)  
    
  
           
def main(cfgname):
    paras=["",""]
    paras[0]=sys.argv[1]
    paras[1]=sys.argv[2]        
    white_dict={}
    
    print paras    
    dealfile(paras,white_dict)  

if __name__ == '__main__':
    main('mainsub.cfg')

