#coding=utf-8
'''
Created on 2019年3月1日

@author: 18588
'''
alien_color="red"
if alien_color=="green":
    print("congratulate you get 5 points")
elif alien_color=="yellow":
    print("congratulate you get 10 points")
elif alien_color=="red":
    print("congratulate you get 15 points")
favorite_fruits=["apple","banana","orange"]
if 'apple'  in favorite_fruits:
    print("you really like bananas")
if 'orange' in favorite_fruits:
    print("you really like bananas")

current_users=["john","lei","hanmeimei","aha","grenn"]
new_users=["jan","lili","lei","john","ouya"]
for user in new_users:
    if new_users:
        if user in current_users:
            print(user +" your name is used")
        else:
            print(user + " your name is new")