#coding=utf-8
'''
Created on 2019年2月28日

@author: 18588
'''
nums=list(range(1,100))
count=0
# for num in nums:
#     print(num)
for num in nums:
    count=count+1.0/num
print(count)