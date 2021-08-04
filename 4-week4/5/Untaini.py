n = int(input())
vList = list(map(int, input().split()))
rangeList =[0]*n
leftGroup = [0]*100002
rightGroup = [0]*100002
disFromRoot = [0]*100002

def findLeft(num):
	if leftGroup[num] != num:
		leftGroup[num] = findLeft(leftGroup[num])
	return leftGroup[num]
		
def findRight(num):
	if rightGroup[num] != num :
		rightGroup[num] = findRight(rightGroup[num])
	return rightGroup[num]
		
for cnt in range(100002):
	leftGroup[cnt] = rightGroup[cnt] = cnt
	
for cnt in range(n-1,-1,-1):
	v = vList[cnt]
	left, right = findLeft(v-1), findRight(v+1)
	leftGroup[v], rightGroup[v] = left, right
	rangeList[cnt] = [left, right]
	findLeft(right-1)
	findRight(left+1)

res=0
resList=[]
for cnt in range(n):
	v, left, right = vList[cnt], rangeList[cnt][0], rangeList[cnt][1]
	disFromRoot[v] = max(disFromRoot[left], disFromRoot[right])+1
	res += disFromRoot[v]-1
	resList.append(str(res))
print("\n".join(resList))