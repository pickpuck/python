#coding=utf-8
'''
Created on 2019年3月3日

@author: 18588
'''
class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=5
    def describe_restaurant(self):
        print("our hotel detail: " + self.restaurant_name + self.cuisine_type)
    def open_restaurant(self):
        print("we are open")
    def set_number_served(self,number_served):
        self.number_served=number_served
    def increment_number_served(self,increment):
        return self.number_served+increment

myRestaurant=Restaurant("rujia","A")
myRestaurant.describe_restaurant()
myRestaurant.open_restaurant()
print(myRestaurant.number_served)
print(myRestaurant.increment_number_served(10))