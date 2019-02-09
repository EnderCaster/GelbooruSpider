#!/usr/bin/env python3
#-*- coding:utf8 -*-
from lxml import etree
from Parser import Parser
import re
class GelbooruParser(Parser):
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
    def getRealImageurl(self, text):
        imageParam = self.getRealImageParams(text)
        print(imageParam)
        img_url = imageParam["domain"]+"/"+imageParam["base_dir"] + \
            "/"+imageParam["dir"]+"/"+imageParam["img"]
        return img_url