#!/usr/bin/env python3
#-*- coding:utf8 -*-
class AimImages:
    def __init__(self):
        self.table_header=['URL','Source Link','Tag List','Rating']
        self.url=''
        self.source=''
        self.tags=''
        self.rating=''
        self.url_file_name='record'
        self.url_file_extension='.csv'
    def save(self):
        line=[]
        line.append(self.url)
        line.append(self.source)
        line.append(self.tags)
        line.append(self.rating)
        file_name=self.url_file_name
        if len(self.rating)>0:
            file_name=file_name+"-"+self.rating.split(':')[1].strip()
        file_name=file_name+self.url_file_extension
        import os
        if not os.path.exists(file_name):
            with open(file_name,'w') as f:
                f.write(",".join(self.table_header)+"\n")
                
        with open(file_name,"a") as record:
            record.write(",".join(line)+"\n")
    