#!/usr/bin/env python
# coding=utf-8

import requests 
import time
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
stopwords = set(STOPWORDS)
stopwords.add("gt")
stopwords.add("如懿传")
stopwords.add("如懿")
stopwords.add("甄嬛传")
stopwords.add("金枝欲孽")
stopwords.add("延禧攻略")
def main(page_number):
        
    url = 'https://movie.douban.com/subject/25812730/comments?start=' + page_number + '&limit=20&sort=new_score&status=P'
    headers = {
        'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'Cookie':'ll="108090"; bid=7SwLSFfk2GU; __utma=30149280.1402903220.1544874589.1544874589.1544874589.1; __utmc=30149280; __utmz=30149280.1544874589.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _ga=GA1.2.1402903220.1544874589; _gid=GA1.2.954301433.1544874590; ps=y; dbcl2="157415839:thCrLy8a/VY"; ck=Em4i; ap_v=0,6.0; push_doumail_num=0; __utmv=30149280.15741; push_noty_num=0; __utmb=30149280.6.10.1544874589; __utma=223695111.1402903220.1544874589.1544874651.1544874651.1; __utmb=223695111.0.10.1544874651; __utmc=223695111; __utmz=223695111.1544874651.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544874651%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E5%25BB%25B6%25E7%25A6%25A7%25E5%25AE%25AB%25E7%2595%25A5%22%5D; _pk_ses.100001.4cf6=*; __yadk_uid=wqSooQ0KGJ9U2dUz507stFMvJ1nfwxvL; _vwo_uuid_v2=DBF7F318DD7A94C24FBF6251F436A95F7|4f2932f8ccc0e0304d67e233fdfa00dc; _pk_id.100001.4cf6=8e90fe50e671c0da.1544874651.1.1544874676.1544874651.',
        'Host':'movie.douban.com'
    }
    r = requests.get(url,headers=headers)
    pattern = re.compile('<span class="short">(.*?)</span>',re.S)
    results = re.findall(pattern,r.text)

    with open('如懿传.txt','a') as file :
        for result in results :
            file.write(result)
            file.write('\n')
            file.write('\n')

for i in range(25):
    main(str(i * 20))
    time.sleep(1)

with open('如懿传.txt') as f:
    text = f.read()
    wordcloud = WordCloud(stopwords='如懿传',width=3500,height=2000,background_color='white',font_path='./simfang.ttf').generate(text)
    plt.figure(dpi=256)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./如懿传.png')
    plt.show()

