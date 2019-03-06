#coding=utf-8
'''
Created on 2019年3月6日

@author: 18588
'''
from collections import OrderedDict
from random import randint
girls=OrderedDict()
girls['lile']="B"
girls['qiongfang']="A"
girls["chenle"]="C"

for key,value in girls.items():
    print(key+" : " + value)
    
boys={}
boys['lile']="B"
boys['qiongfang']="A"
boys["chenle"]="C"
for key,value in boys.items():
    print(key+" : " + value)
    
print(randint(1,1000))