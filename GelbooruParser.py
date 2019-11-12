#!/usr/bin/env python3
#-*- coding:utf8 -*-
from lxml import etree
from Parser import Parser
import re
class GelbooruParser(Parser):
    def __init__(self,html):
        self.html=html
    def getRealImageParams(self, content):
        content = content.replace("\r", "")
        textArr = content.split("\n")
        imageParam = dict()
        for line in textArr:
            line = line.strip()
            if line.startswith("image ="):
                content = line.split('{')[1].split('}')[0]
                params = content.split(',')
                for param in params:
                    paramExchange = param.split("\':\'")
                    imageParam[paramExchange[0].replace("\'", '').strip(
                    )] = "".join(paramExchange[1:2048]).replace("\'", '').strip()
                break
        return imageParam
    def getUrlParam(self, url, name):
        params = url.split('?')[-1].split('&')
        result = {}
        result.setdefault(name, 0)
        for param in params:
            exchange = param.split('=')
            result[exchange[0]] = exchange[1]
        return result[name]
    def getRealImageurl(self):
        imageParam = self.getRealImageParams(self.html)
        print(imageParam)
        img_url = imageParam["domain"]+"/"+imageParam["base_dir"] + \
            "/"+imageParam["dir"]+"/"+imageParam["img"]
        return img_url
    def getImageParams(self):
        url=self.getRealImageurl()
        source=self.xpath(self.html,'//*/li[contains(text(),"Source")]/a/@href')
        source=self.processParam(source)
        tags=self.xpath(self.html,'//*/img/@alt')
        tags=self.processParam(tags)
        rating=self.xpath(self.html,'//*/li[contains(text(),"Rating")]/text()')
        rating=self.processParam(rating)
        return (url,source,tags,rating)

    def processParam(self,param):
        if len(param)>0:
            return param[0]
        return ''
    def setHTML(self,html):
        self.html=html