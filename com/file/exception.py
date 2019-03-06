# coding=utf-8
'''
Created on 2019年3月6日

@author: 18588
'''
import json
text = 'now you type:'
try:
    pro = int(input(text))
except ValueError:
        print("please input some string")
else:
    print("the number is %d" % pro)

