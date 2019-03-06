#coding=utf-8
'''
Created on 2019年1月2日

@author: 18588
'''
letters=['linda','adam','chen','messa']
print(letters)
print(letters[0])
print(letters[-1])
letters[0]='lile'
print(letters)
letters.append('jinang xue')
print(letters)
letters.insert(-1,'che che')
print(letters)
#del需要知道列表元素位移
del(letters[-1])
letters.pop()
print(letters)
letters.remove('adam')

print(letters)
letters.append('LI')
#letters.sort(reverse=True)

print(sorted(letters))
letters.reverse()
print(letters)
for a in letters:
    print a