# 广州市政府采购平台
# -*- coding: utf-8 -*-
# code by leiz

import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool
from pub import pachong
import json




def Main():
    head='http://gzg2b.gzfinance.gov.cn'

    with open('./广州市政府采购平台/info.csv','wt') as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(['类型','网址','名称','时间'])

        url='http://gzg2b.gzfinance.gov.cn/gzgpimp/portalsys/portal.do?method=queryHomepageList&t_k=null'
        for i in range(1,10):
            params={'current': i,'rowCount': 10,'searchPhrase':'' ,'title_name':'' ,'porid': 'gsgg','kwd':'' }
            print(url)
            j=json.loads(pachong.getChinabiddingHtml(url,pachong.headers,params))
            print(j)
            for row in range(100):
                # print(j['rows'][row]['info_key'])
                csvWriter.writerow([j['rows'][row]['info_key'],j['rows'][row]['info_path'],j['rows'][row]['title'],j['rows'][row]['update_time']])
            f.flush()
    return


if __name__=='__main__':

    Main()