#coding=utf-8
'''
Created on 2019年3月2日

@author: 18588
'''
def display_message():
    print("we code hanshu")
def favorite_book(title):
    print("we like the book: "+title.title())
def make_shirt(size,text="I Love Python"):
    print("we made a shirt,and the size is "+size+",the text on it is "+text)
def describe_city(name,country="china"):
    print(name+" is in "+country)
def city_country(city,country):
    print(city + " is in " + country)
def make_album(singer,album,num=" "):
    albums={}
    albums['singer']=singer
    albums['album']=album
    if num!=" ":
        albums['num']=num
#     print(albums)
    return albums
display_message()
favorite_book("houtian")
make_shirt("12L","天才")
make_shirt("big")
describe_city("guangzhou")
describe_city("newyork", country="usa")
i=0
# while True:
#     city=input("please input a city name:")
#     country=input("please input a country name:")
#     city_country(city,country)
#     i=i+1
#     if i>=3:
#         break
#字典
album1=make_album("lidaimo", "shiguang")
album2=make_album("linqingfeng", "shuimunianhua",3)
album3=make_album("zhangqiyangzi", "shaonianyou")
print(album1)
print(album2)


