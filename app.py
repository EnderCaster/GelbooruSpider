#!/usr/bin/env python3
#-*- coding:utf8 -*-
import requests as req
import time
from GelbooruParser import GelbooruParser
from SETTINGS import SETTINGS
from AimImages import AimImages
from random import random
import argparse
from urllib import parse
def judge(content,index_count):
    parser=GelbooruParser(content)
    page_list=parser.xpath(content,'//div[@class="pagination"]/a/@href')
    try:
        max_page=int(page_list[-1])
        return max_page<index_count
    except:
        print("exception")
        return False


arg_parser=argparse.ArgumentParser()
arg_parser.add_argument('keyword')
args=arg_parser.parse_args()
keyword=parse.quote(args.keyword)

start_url="https://gelbooru.com/index.php?page=post&s=list&tags="+keyword
headers={"Connection":"close"}
resp=req.get(start_url)
index_count=0
page_content_count=42
parser=GelbooruParser(resp.text)
temp=0
while resp:
    image_list=parser.xpath(resp.text,'//span[@class="thumb"]/a/@href')
    for image_url in image_list:
        image_url="https:"+image_url
        resp_image_post=req.get(image_url,headers=headers)
        parser.setHTML(resp_image_post.text)
        url,source,tags,rating=parser.getImageParams()
        image=AimImages(keyword=keyword)
        image.url=url
        image.source=source
        image.tags=tags
        image.rating=rating
        image.save()
        # time.sleep(SETTINGS.DELAY_BASE+3*random())
        
        
    index_count+=1
    pid=index_count*page_content_count
    next_url=start_url+"&pid="+str(pid)
    
    if judge(resp.text,index_count):
        resp=None
    else:
        resp=req.get(next_url)
