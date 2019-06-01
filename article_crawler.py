# encoding=utf8
import sys
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import re
import pymongo
import random
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def countchn(string):
    pattern = re.compile(u'[\u1100-\uFFFDh]+?')
    result = pattern.findall(string)
    chnnum = len(result)
    possible = chnnum/len(str(string))
    return (chnnum, possible)

def getHtml():
    client = pymongo.MongoClient('localhost', 27017)
    mydb = client['a_stock']
    collection = mydb.get_collection('a_news_company')
    file = open('my_astock_all_news_url.csv', 'r')
    df = pd.DataFrame(columns=['title','url','label_property','code','company','article'])
    lines = file.readlines()
    j = 0
    for line in lines:
        stocks = line.split(',')
        url = stocks[1].strip();
        label_property = stocks[2].strip();
        title = stocks[0].strip();
        code = stocks[3].strip();
        company = stocks[4].strip();

        print(url)
        article =''
        #proxies = {'https':'https://{}'.format(random.choice(proxy_pool))}
        #print(proxies)
        try:

            html = requests.get(url, headers = headers,);
            time.sleep(2)
            bs = BeautifulSoup(html.text, "lxml")
            part = bs.find_all('p')
            for paragraph in part:
                article += str(paragraph.get_text())
                '''
                chnstatus = countchn(str(paragraph))
                possible = chnstatus[1]
                if possible > 0.1 and u'免责声明' not in str(paragraph):
                   article += str(paragraph)
                '''
            #print(article)
            data_df = {'title':title,'url':url,'label_property':label_property,'code':code,'company':company,'article':article}
            collection.insert_one(data_df)

        except Exception:
            continue
            #data_df = {'title':title,'url':url,'label_property':label_property,'code':code,'company':company,'article':''}
            #collection.insert_one(data_df)


getHtml()
