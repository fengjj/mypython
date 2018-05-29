# coding: UTF-8
'''
Created on 2016年10月26日

@author: fengjj
'''
def main():

    fileObj = open('C:\\Users\\fengjj\\Desktop\\4gfeecode.txt')
    output = open('C:\\Users\\fengjj\\Desktop\\deal_4gfeecode.txt','wt')
    feeType = 2
    for line in fileObj:
        print(line)
        tmp = line.split(',')
        if len(tmp)>1:
            fee = tmp[0]
            data = getData(tmp[1])
            #INSERT INTO `mk_fee_info` VALUES ('1001', '0', 0, '1', '3');
            output.writelines('INSERT INTO `mk_fee_info` VALUES (\''+fee+'\',\'2\',\''+str(data)+'\',\'1\',\'4\');\n')
    fileObj.close()
    output.close()
def getData(str):
    if str.find('200M')!=-1:
        return 200*1024*1024
    if str.find('500M')!=-1:
        return 500*1024*1024
    if str.find('3G')!=-1:
        return 3*1024*1024*1024
    if str.find('1G')!=-1:
        return 1024*1024*1024
    if str.find('15G')!=-1:
        return 15*1024*1024*1024
    if str.find('6G')!=-1:
        return 6*1024*1024*1024
if __name__ == '__main__':
    main()