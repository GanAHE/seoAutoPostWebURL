#!usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup as bp


def getSitemap(sitemapLink,saveAddress):
    print('push site is opening now....')
    time.sleep(0.5)
    site_url = sitemapLink

    try:
        print('get sitemap link....','utf-8')
        data_ = bp(requests.get(site_url).content,'lxml')
    except Exception as e:
        print(e)

    list_url = []
    print('---------------------------------')
    for x,y in enumerate(data_.find_all('loc')):
        print(x,y.string)
        list_url.append(y.string.replace('http://','https://www.'))

    print('---------------------------------')

    print('Lisy',list_url)


    target = saveAddress
    try:
        with open(target,"w") as f:
            for i in range(len(list_url)):
                f.write(list_url[i]+"\n")
        print("写入完成,路径{}\n 6s后自动关闭".format(target))
        time.sleep(5)
    except Exception as e:
        print("ERROR! ",e.__str__())
