from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = 'https://movie.douban.com/chart'
headers = {
            'Cookie': 'bid=cZtGoTwQIZQ; douban-fav-remind=1; viewed="5353163"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1624939797%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fmovie.douban.com%2Fchart%22%5D; _pk_ses.100001.4cf6=*; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; ll="108099"; _pk_id.100001.4cf6=e4c925697dbd3874.1624939797.1.1624941283.1624939797.; __utma=30149280.605274653.1624702696.1624939797.1624941283.4; __utmb=30149280.0.10.1624941283; __utmz=30149280.1624941283.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.308538011.1624939797.1624939797.1624941283.2; __utmb=223695111.0.10.1624941283; __utmz=223695111.1624941283.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _vwo_uuid_v2=DAB8E4309F7846ED2B1CCA283ADDAF7BB|0614716c3aa732f9c6f5d977570c2fc8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
f = requests.get(url, headers)
print(f)
print(f.content)#Get该网页从而获取该html内容

soup = BeautifulSoup(f.content, "lxml") #用lxml解析器解析该网页的内容, 好像f.text也是返回的html

for k in soup.find_all('div',class_='pl2'):#,找到div并且class为pl2的标签
    a = k.find_all('span') #在每个对应div标签下找span标签，会发现，一个a里面有四组span
    print(a[0].string) #取第一组的span中的字符串