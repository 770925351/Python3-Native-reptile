#!/usr/bin/env python
# coding=utf-8
''' 导入requests库 '''
import requests
import re
import time
movies = []
number = 1
def main(offet,number):
    url = 'https://maoyan.com/board/4?offset=' + str(offet)
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'    
    }
    r = requests.get(url,headers=headers)

    results = re.findall('<p class="name">.*?>(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>',r.text,re.S)

    for result in results:
        movie = {}
        movie['排名'] = number
        movie['电影名称'] = result[0]
        movie['演员'] = result[1].strip()
        movie['上映时间'] = result[2]
        movie['分数'] = result[3] + result[4]
        movies.append(movie)
        number += 1

for i in range(10):
    main(i * 10,number)
    number += 10
    time.sleep(1)

with open('result.txt','w') as file:
    for x in movies:
        for key,value in x.items():
            file.write(key + ":" + str(value) + " ")
        file.write('\n')
