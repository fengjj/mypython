import ConfigParser 
import string, os, sys
import paramiko
import re
import time,datetime


  
           
def main():
    file_object=open("lacci",'r')
    out_file=open("lacciout",'w')
    for line in file_object:
        print line
        lacci=hex(int(line.split(',')[0])).upper()[2:]+hex(int(line.split(',')[1])).upper()[2:]
        out_file.writelines("%s\n" % lacci)
    out_file.close()
    file_object.close()                   

if __name__ == '__main__':
    main()


