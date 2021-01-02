#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author    :GanAHE
# @Time      :2021/1/2 17:27
# @contact   :dgzc.ganahe.top

#coding:utf-8
import requests
import time
from bs4 import BeautifulSoup as bp


def push(site):
    print('push site is opening now....')
    time.sleep(0.5)
    sitemap_url = site["sitemapLink"]

    try:
        print('get sitemap link....','utf-8')
        data_ = bp(requests.get(sitemap_url).content,'lxml')
    except Exception as e:
        print(e)

    list_url=[]

    print('---------------------------------')
    for x,y in enumerate(data_.find_all('loc')):
        print(x,y.string)
        list_url.append(y.string.replace('http://','https://www.'))

    print('---------------------------------')

    print('pushing....')
    xmlData = {"siteUrl":site["url"],"urlList":list_url}
    postTheXML(site["baiduAPIUrl"],xmlData)
    print("推送完成,6s后自动关闭....")
    time.sleep(6)

def postTheXML(apiUrl, data):
    headers={"Host": "ssl.bing.com",
             'Content-Type':'application/json'}
    try:
        r = requests.post(url=apiUrl,data=data)
        print(r.status_code)
        print(r.content)
    except Exception as e:
        print(e)

