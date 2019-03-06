#coding=utf-8
'''
Created on 2019年3月7日

@author: 18588
'''
import json

with open("test.txt") as zhe:
    txt=json.load(zhe)
    print(txt)