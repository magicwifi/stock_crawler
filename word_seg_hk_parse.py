# encoding=utf8
import sys
import requests






# your spider code

def getHtml():
    file = open('stock_title_train.csv', 'r')
    write_file = open('stock_noun_train.csv', 'w')
    lines = file.readlines()
    for line in lines:
        line=line.strip()
        stocks = line.split(',')
        if len(stocks) == 2:
            words = stocks[1]
            nouns = stocks[0].split();
            words_length = len(words)
            nouns_length = len(nouns)
            #print(words_length)
            #print(nouns_length)
            if words_length == nouns_length:
                for i in range(0,nouns_length):
                    if words[i].strip()=="":
                        words_tmp = ','
                    else:
                        words_tmp = words[i]
                    write_file.write(words_tmp+'\t'+nouns[i]+'\n')
                write_file.write('\n')
            else :
                continue;
        else:
            continue;
    write_file.close()

getHtml()
