#!/usr/bin python
#! backup system files

import time
import os
import sys
d_dir='/usr/local/py/backup/'    #备份目标目录
d_files='system_back.tar.gz'    #命名文件

s_dir =['/etc/','/usr/local/mongodb/']    #源目录
data=time.strftime('%Y%m%d')    #时间
d_dir1 = d_dir + data + '/'        #创建时间的目录
r_name = d_dir1 + d_files        #压缩文件所在的目录以及名字

def all_bak():        #写到函数里面
    print ('backup scripts start,please wait ...')
    print ('\033[32m--------------------------------------------\033[0m')
    time.sleep(2)    #等待两秒

    if os.path.exists(d_dir1) == False:
            os.makedirs(d_dir1)
            print ('Successfully create {0}!'.format(d_dir1))
    else:
            print ('the dir {0} is exists !'.format(d_dir1))

    tar_dir = 'tar -czvf {0} {1} '.format(r_name,' '.join(s_dir))    #定义备份文件
    if os.system(tar_dir) == 0:        #执行备份的命令
        print ('the backup files {0} is successfully!').format(r_name)        #打印出来备份的目录
    else :
        print ('the backup files is falsed!')
try:                                #不输入参数的时候处理异常
    if len(sys.argv[1]) == 0:
        pass
except IndexError:
        print ('warning:{please exec {0} help|all_bak}'.format(sys.argv[0]))
try:                                 #输入参数的时候处理异常
    if sys.argv[1] == 'all_bak':
        all_bak()                    #输入参数为all_bak的时候执行备份
    else:
        print ('warning:{please exec {0} help|all_bak}'.format(sys.argv[0]))    
except IndexError:
    pass
