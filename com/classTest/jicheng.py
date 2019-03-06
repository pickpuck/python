#coding=utf-8
'''
Created on 2019年3月5日

@author: 18588
'''
from dog import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors=[]):
        super(IceCreamStand,self).__init__(restaurant_name, cuisine_type)
        self.flavors=flavors
    def iceCream(self):
        for flavor in self.flavors:
            print(flavor)
    def describe_restaurant(self):
        print("we are icecream,not hotel")

flavors=["apple","green","cola"]
myIceCreamStand=IceCreamStand("lifeng","5A",flavors)
myIceCreamStand.iceCream()
myIceCreamStand.describe_restaurant()
