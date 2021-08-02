n=int(input())
arr=[]
for i in range(n):
    arr.append(i+1)

while True:
    if len(arr)==1:
        print(arr[0])
        return
    temp=[]
    for i in range(1,len(arr)+1):
        if i%2==0:
            temp.append(arr[i-1])
    arr=temp
    
