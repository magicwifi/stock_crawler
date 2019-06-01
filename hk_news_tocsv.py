# encoding=utf8
import sys
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# your spider code

def getHtml():
    df = pd.DataFrame(columns=['title','url','ctime', 'label_type','label_property','label_article','code','company','industry'])
    file = open('h_tmp.csv', 'r')
    lines = file.readlines()
    j = 0
    for line in lines:
        stocks = line.split(',')
        code = stocks[0].strip();
        company = stocks[1].strip();
        industry = stocks[3].strip();

        for i  in range(1,4):
            value = 'https://m.0033.com/listv4/hk/'+code+'_'+str(i)+'.json'
            html = requests.get(value, headers = headers)
            results = json.loads(html.text)
            try:
                pageItems = results['data']['pageItems']
                for pageItem in pageItems:
                    title = pageItem['title']
                    ctime = pageItem['ctime']
                    label_type = pageItem['label_type']
                    label_property = pageItem['label_property']
                    label_article = pageItem['label_article']
                    url = pageItem['url']
                    #print(title)
                    df.loc[len(df)] = {'title':title,'url':url,'ctime':ctime,'label_type':label_type,'label_property':label_property,'label_article':label_article,'code':code,'company':company,'industry':industry}
                    if len(df)  % 10000 ==0:
                        df.to_csv('my_hk_news'+str(j)+'.csv',index=None)
                        j = j+1
                        df = df.iloc[0:0]
                        df = pd.DataFrame(columns=['title','url','ctime', 'label_type','label_property','label_article','code','company','industry'])

            except Exception:
                continue;
    df.to_csv('my_hk_news'+str(j)+'.csv',index=None)

getHtml()
