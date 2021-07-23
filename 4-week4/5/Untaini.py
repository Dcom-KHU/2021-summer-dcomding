from sys import stdin

fenwickTree = [0]*100003
distanceFromRoot = [0]*100003
n=int(stdin.readline())+2
v=list(map(int, stdin.readline().split()))

def update(num, val):
	while num<=n:
		fenwickTree[num] += val
		num += (num & -num)
	return
		
def getRange1ToNum(num):
	res=0
	while num>0:
		res += fenwickTree[num]
		num -= (num & -num)
	return res
		
def binarySearch(val):
	left = 1
	right = n
	while left<=right:
		mid = (left+right)//2
		if getRange1ToNum(mid) <= val:
			left = mid+1
		else :
			right = mid-1
	return left
	
res=0
res_str = ""
update(1,1)
update(n,1)
for i in range(n-2):
	val=v[i]+1
	rangeVal = getRange1ToNum(val)
	left = binarySearch(rangeVal-1)
	right = binarySearch(rangeVal)
	distanceFromRoot[val] = max(distanceFromRoot[left], distanceFromRoot[right]) + 1
	res += distanceFromRoot[val] - 1
	res_str += str(res)+"\n"
	update(val,1)
print(res_str)
