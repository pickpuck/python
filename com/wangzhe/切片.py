#coding=utf-8
'''
Created on 2019年2月26日

@author: 18588
'''
friends=['linda','lile','qiongfang','bili','zengqingqing']
print(friends[-3:])
print(friends[1:3])
girl_friends=friends[:]
print(girl_friends)
print('The first thiree items in the list are:' )
for friend in friends[:3]:
    print(friend)
