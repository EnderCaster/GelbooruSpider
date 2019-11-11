#!/usr/bin/env python3
#-*- coding:utf8 -*-
class AimImages:
    url_file_name="url.txt"
    def __init__(self,url,source,tags):
        self.url=url
        self.source=source
        self.tags=tags
    def save(self):
        with open(self.url_file_name,"a") as record:
            record.write(self.url+","+self.source+"\n")
    