import requests
from bs4 import BeautifulSoup

class pachong():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        , 'Accept-Language': 'zh-CN,zh;q=0.9'
        , 'Accept-Encoding': 'gzip, deflate, br'
        ,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        , 'Host': 'www.chinabidding.cn'
        , 'Connection': 'keep-alive'
        , 'Cache-Control': 'max-age=0'}

    def getChinabiddingHtml(self,url, headers, params=''):
        s = requests.Session()
        for i in range(3):
            try:
                resp = s.get(url, headers=headers, params=params, timeout=10)
            except:
                print('timeout for {}'.format(i + 1))
        if resp.status_code == 200:
            return BeautifulSoup(resp.content, 'html5lib')
        else:
            print(resp.status_code)
            return None

if __name__=='__main__':
    p=pachong()
    print(pachong.headers)