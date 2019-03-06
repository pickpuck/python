#coding=utf-8
'''
Created on 2019年3月2日

@author: 18588
'''
favor_nums={"john":"1","lei":14,"guoguo":15}
print(favor_nums["john"])
print(favor_nums["lei"])
print(favor_nums["guoguo"])
#添加键值
favor_nums['wangzhe']=18
favor_nums['yunlong']=19
print(favor_nums)
del favor_nums['john']
print(favor_nums)
#遍历
rivers={"zhujiang":"guangzhou","nile":"egypt","juanshui":"shuangfeng"}
for key,value in rivers.items():
    print("the "  + key +" runs through " + value)
for key in rivers.keys():
    print(key +"\n")
for value in rivers.values():
    print(value+"\n")
#字典嵌套
cities={"guangzhou":"","shenzhen":"","dongguan":""}
cities['guangzhou']={"country":"china","population":"13million","text":"china"}
cities['shenzhen']={"country":"china","population":"13million","text":"china"}
cities['dongguan']={"country":"china","population":"13million","text":"china"}
print(cities)
