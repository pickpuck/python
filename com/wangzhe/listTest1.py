#coding=utf-8
'''
Created on 2019年2月18日

@author: 18588
'''
guest=["qiong","fang","wangzhe"]
print(guest[1]+" can't attend it")
guest[1]="lile"
for a in guest:
     print(a+" will attend the party")
#add 3 role
guest.append("chenle")
guest.insert(2,"xiaohong")
guest.insert(0, "gexi")
for a in guest:
    print("we get a bigger table," +a +" will attend the party")
print("we are sorry,and only 2 can join")
print(guest)
print(guest.pop(2) + " can't join it")
print(guest.pop(2) + " can't join it")
print(guest.pop(2) + " can't join it")
print(guest.pop(2) + " can't join it")
for a in guest:
    print(a + " will join it")
del guest[0]
del guest[0]
print guest