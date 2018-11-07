# 广州市政府采购平台

import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool
from getBidInfo import getChinabiddingHtml
from getBidInfo import headers



def Main():
    head='https://www.chinabidding.cn'

    with open('./广州市政府采购平台/info.csv','wt') as f:
        csvWriter=csv.writer(f)
        # csvWriter.writerow(['','项目名称','是否收藏','类型','省份','行业','时间','网址'])

        url='http://gzg2b.gzfinance.gov.cn/gzgpimp/portalsys/portal.do?method=queryHomepageList&t_k=null'
        params={'current': 2,'rowCount': 10,'searchPhrase':'' ,'title_name':'' ,'porid': 'gsgg','kwd':'' }
        print(url)
        bsObj=getChinabiddingHtml(url,headers,params=params)
        print(bsObj,file=f)
    return


if __name__=='__main__':

    Main()