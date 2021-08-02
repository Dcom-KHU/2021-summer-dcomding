n=int(input())
arr=[]
for i in range(n):
    arr.append(i+1)

while len(arr)!=1:
    temp=[]
    for i in range(1,len(arr)+1):
        if i%2==0:
            temp.append(arr[i-1])
    arr=temp
    
print(arr[0])