import pandas as pd
import csv
for i in range(1,80):  # 爬取全部177页数据
    url = 'http://s.askci.com/stock/h/?reportTime=2019-04-30&pageNum=%s' % (str(i))
    tb = pd.read_html(url)[3] #经观察发现所需表格是网页中第4个表格，故为[3]
    tb.to_csv(r'h.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    print('第'+str(i)+'页抓取完成')
