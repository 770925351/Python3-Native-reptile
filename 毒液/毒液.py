#!/usr/bin/env python
# coding=utf-8
import requests 
import time
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main(page_number):
        
    url = 'https://movie.douban.com/subject/3168101/comments?start=' + page_number + '&limit=20&sort=new_score&status=P'
    headers = {
        'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie':'bid=Xr5ygOF-E5Y; ll="118088"; __utmc=30149280; __utmz=30149280.1544792217.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmc=223695111; __utmz=223695111.1544792219.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=X1C3e3FZr2W6oWHuo62JVExOXJtfEs40; _vwo_uuid_v2=D3E7F5595A0DCC633294CB68F6288FC5B|1aba894100aacf621dddc14cc5b79cb0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544795624%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.451707390.1544792217.1544792217.1544795624.2; __utmt=1; ps=y; __utma=223695111.294464458.1544792219.1544792219.1544795640.2; __utmb=223695111.0.10.1544795640; __utmb=30149280.4.10.1544795624; dbcl2="157415839:thCrLy8a/VY"; ck=Em4i; push_doumail_num=0; push_noty_num=0; _pk_id.100001.4cf6=6184ed17f1c74804.1544792219.2.1544795849.1544792739.'
    }
    r = requests.get(url,headers=headers)
    pattern = re.compile('<span class="short">(.*?)</span>',re.S)
    results = re.findall(pattern,r.text)

    with open('毒液.txt','a') as file :
        for result in results :
            file.write(result)
            file.write('\n')
            file.write('\n')

for i in range(25):
    main(str(i * 20))
    time.sleep(1)

with open('毒液.txt') as f:
    text = f.read()
    wordcloud = WordCloud(width=3500,height=2000,background_color='white',font_path='./simfang.ttf').generate(text)
    plt.figure(dpi=256)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.savefig("毒液.png")

