#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(100+299+399)

n = 123
f=456.789
s1='中文现实'
s2='Hello,\'Adam\''
s3=r'Hello,"Bart"'
s4=r'''Hello,
Lisa!'''
print(s1)
print(f)
print(s2,s3,s4)

a1=input('上次的成绩\n')
a2=input('这次的成绩\n')
a3=(int(a2)/int(a1)-1) * 100
print(a3)
if a3 > 0:
    a5='提高'
else:
    a5='下降'
#a4 = '小明的成绩了：%.2f' % a3
print('小明的成绩',a5,'了：%.1f%%' % a3)



