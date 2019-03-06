#coding=utf-8
'''
Created on 2019年2月18日

@author: 18588
'''
for a in range(1,21):
    print a
#for a in range(1,1000001):
#    print a
millions=list(range(1,1000001))
print(min(millions))
print(max(millions))
print(sum(millions))
#奇数
odds=list(range(1,20,2))
print(odds)
mods=[]
for a in range(1,10):
    mods.append(3*a)
print(mods)
#立方
for a in range(1,10):
    mods.append(a*a*a)
print(mods)
lifangs=[a**3 for a in range(1,10)]
print (lifangs)
    