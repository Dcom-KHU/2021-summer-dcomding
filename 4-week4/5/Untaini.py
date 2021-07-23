from sys import stdin
import operator as o

fenwickTree = o.mul([0],100003)
distanceFromRoot = o.mul([0],100003)
n=o.add(int(stdin.readline()),2)
v=[o.add(int(i),1) for i in stdin.readline().split()]

def update(num, val):
	while o.le(num,n):
		fenwickTree[num] = o.add(fenwickTree[num],val)
		num = o.add(num, o.and_(num, o.neg(num)))
	return
		
def getRange1ToNum(num):
	res=0
	while o.gt(num,0):
		res = o.add(res, fenwickTree[num])
		num = o.sub(num, o.and_(num, o.neg(num)))
	return res
		
def binarySearch(val):
	left = 1
	right = n
	while o.le(left,right):
		mid = o.floordiv(o.add(left,right),2)
		if o.le(getRange1ToNum(mid),val):
			left = o.add(mid,1)
		else :
			right = o.sub(mid,1)
	return left
	
res=0
res_str = ""
update(1,1)
update(n,1)
for val in v:
	rangeVal = getRange1ToNum(val)
	left = binarySearch(o.sub(rangeVal,1))
	right = binarySearch(rangeVal)
	distanceFromRoot[val] = o.add(max(distanceFromRoot[left], distanceFromRoot[right]),1)
	res = o.add(res, o.sub(distanceFromRoot[val],1))
	res_str = o.add(res_str, o.add(str(res),"\n"))
	update(val,1)
print(res_str)
