# -*- coding:utf-8*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import os.path
import time
time1=time.time()

def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'a+')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath)
            k.write(f.read()+"\n")

    k.close()




if __name__ == '__main__':
    filepath="/Users/zhuangzhuanghuang/Code/stock_crawler/a_stock_news/"
    outfile="result.txt"
    MergeTxt(filepath,outfile)
    time2 = time.time()

