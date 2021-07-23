from sys import stdin

fenwickTree = [0]*100003
distanceFromRoot = [0]*100003
n=int(stdin.readline())+2
v=[int(i)+1 for i in stdin.readline().split()]
bitList = [0]*100003
for i in range(1,100003):
	exp = 2
	while not i%exp: exp*=2;
	bitList[i] = exp//2

def update(num, val):
	while num<=n:
		fenwickTree[num] += val
		num += bitList[num]
	return
		
def getRange1ToNum(num):
	res=0
	while num>0:
		res += fenwickTree[num]
		num -= bitList[num]
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
for val in v:
	rangeVal = getRange1ToNum(val)
	left = binarySearch(rangeVal-1)
	right = binarySearch(rangeVal)
	distanceFromRoot[val] = max(distanceFromRoot[left], distanceFromRoot[right]) + 1
	res += distanceFromRoot[val] - 1
	res_str += str(res)+"\n"
	update(val,1)
print(res_str)
