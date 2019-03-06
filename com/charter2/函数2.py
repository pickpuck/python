#coding=utf-8
'''
Created on 2019年3月3日

@author: 18588
'''
def show_magicians(magicians):
    for magician in magicians:
        if magicians:
            print("magician's name is: " + magician)
def make_great(magicians):
    i=0
    while i<len(magicians):
            magicians[i]= "the great".title()+" " +magicians[i]
            i=i+1
    return magicians
      
magicians=["melady","adam","april"]
a=make_great(magicians[:])
show_magicians(a)
show_magicians(magicians)