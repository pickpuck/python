# coding=utf-8
'''
Created on 2019年3月6日

@author: 18588
'''
with open("test.txt") as test:
#     lines=test.read()
#     print(lines.rstrip())
#     for line in lines:
#         print(line)
    a_lines = test.readlines()
for line in a_lines:
    new_line = line.replace('Python', 'C++')
    print(new_line),

str = "I love you"
new_str = str.replace('you', 'she')
print('\n' + new_str)
print("we say :%s" % (new_str))

# 写入文件
with open("wang1.txt", "a") as wang:
    while True:
        input1 = "please type some charactor:"
        pro = input(input1)
        wang.write(pro)
#         print(wang.readlines())
#     wang.write("123")
