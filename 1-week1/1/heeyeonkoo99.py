#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1주차 수업-1
n,k=map(int,input().split())
temp=list(map(int,input().split()))
idx=0
while idx!=k:
    if idx%2==0:
        temp.remove(min(temp))
    else:
        temp.remove(max(temp))
    idx+=1
print(sum(temp))
