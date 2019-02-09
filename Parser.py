#!/usr/bin/env python3
#-*- coding:utf8 -*-
from lxml import etree
class Parser:
    def xpath(self,text,xpath):
        document=etree.HTML(text)
        return document.xpath(xpath)