#coding=utf-8
'''
Created on 2019年3月2日

@author: 18588
'''
sandwich_orders=["potatoes","tomatoes","apple"]
finished_sandwich=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    finished_sandwich.append(sandwich)
print(sandwich_orders)
print(finished_sandwich)
#7-9
sandwich_orders=["pastrami","potatoes","pastrami","tomatoes","pastrami","apple"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)