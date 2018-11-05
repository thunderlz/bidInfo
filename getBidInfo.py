import requests
from bs4 import BeautifulSoup

def getChinabiddingHtml(url,headers):
    s=requests.Session()
    resp=s.get(url,headers=headers)

    return BeautifulSoup(resp.content,'html5lib')

def Main():
    url='https://www.chinabidding.cn/search/Searchgj/zbcg?table_type=&text_x=%E8%BE%93%E5%85%A5%E6%82%A8%E6%83%B3%E6%9F%A5%E6%89%BE%E7%9A%84%E5%85%B3%E9%94%AE%E8%AF%8D+%E5%A4%9A%E4%B8%AA%E8%AF%8D%E5%8F%AF%E4%BB%A5%E8%BE%93%E5%85%A5%E7%A9%BA%E6%A0%BC%E9%9A%94%E5%BC%80%EF%BC%81&keywords=%E6%8B%9B%E6%A0%87%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1&search_type=TITLE&areaid=&categoryid=&b_date=month&time_start=2018-11-05&time_end=2018-11-05'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        , 'Host': 'www.chinabidding.cn'
        , 'Connection': 'keep-alive'
        , 'Cache-Control': 'max-age=0'}
    with open('bid.html','wt') as f:
        print(getChinabiddingHtml(url,headers).find_all('a'),file=f)
        print(f.buffer)
    return


if __name__ == '__main__':
    Main()
    