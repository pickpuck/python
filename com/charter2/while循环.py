#coding=utf-8
'''
Created on 2019年3月2日

@author: 18588
'''
text="will how many pepole attend the dinner:"
count=int(input(text))
if count>=8:
    print("we are soory,there is no tables")
else:
    print("ok,we can fix up")

#电影票
text="please input your age here:"

while True:
    age=int(input(text))
    if age<3:
        print("you are free")
    elif age>=3 and age<=12:
        print("please insert 10 dollars")
    elif age>12:
        print("pay 15 dollars")

