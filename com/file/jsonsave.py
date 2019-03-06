# coding=utf-8
'''
Created on 2019年3月6日

@author: 18588
'''
import json

with open("test.txt", "w") as test:
    txt = json.dump("abcd", test)
