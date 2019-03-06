#coding=utf-8
'''
Created on 2019年3月3日

@author: 18588
'''
def make_great(magicians):
    i=0
    while i<len(magicians):
            magicians[i]= "the great".title()+" " +magicians[i]
            i=i+1
    return magicians