from sys import stdin
from operator import *

fenwickTree = mul([0],100003)
distanceFromRoot = mul([0],100003)
n=add(int(stdin.readline()),2)
v=[add(int(i),1) for i in stdin.readline().split()]

def update(num, val):
	while le(num,n):
		fenwickTree[num] = add(fenwickTree[num],val)
		num = add(num, and_(num, neg(num)))
	return
		
def getRange1ToNum(num):
	res=0
	while gt(num,0):
		res = add(res, fenwickTree[num])
		num = sub(num, and_(num, neg(num)))
	return res
		
def binarySearch(val):
	left = 1
	right = n
	while le(left,right):
		mid = floordiv(add(left,right),2)
		if le(getRange1ToNum(mid),val):
			left = add(mid,1)
		else :
			right = sub(mid,1)
	return left
	
res=0
resList=[]
resApp = resList.append
update(1,1)
update(n,1)
for val in v:
	rangeVal = getRange1ToNum(val)
	left = binarySearch(sub(rangeVal,1))
	right = binarySearch(rangeVal)
	distanceFromRoot[val] = add(max(distanceFromRoot[left], distanceFromRoot[right]),1)
	res = add(res, sub(distanceFromRoot[val],1))
	resApp(str(res))
	update(val,1)
print("\n".join(resList))
