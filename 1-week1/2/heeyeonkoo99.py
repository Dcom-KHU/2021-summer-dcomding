#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1주차 수업-2
import sys

global movement=[]
answer=0
def hanoi_top(n,a,b,c):
    if n==1:
        movement.append([a,c])
    else:
        hanoi_top(n-1,a,c,b)
        movement.append([a,c])
        hanoi_top(n-1,b,a,c)

n=int(sys.stdin.readline())
hanoi_top(n,1,2,3)

for i in movement:
    answer+=i[1]
    
#print(len(movement)) =>이동횟수
print(answer)


#Review) 설명이 잘나와있다. 헷갈릴때마다 보기=> https://m.blog.naver.com/jaeyoon_95/221762231876
# 프로그래머스 level3에 있는 문제도 풀어보자!
