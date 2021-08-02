n=int(input())
arr=[i+1 for i in range(n)]

while len(arr)!=1:
    temp=[]
    for i in range(len(arr)):
        if (i+1)%2==0:
            temp.append(arr[i])
     
    arr=temp
print(arr[0])