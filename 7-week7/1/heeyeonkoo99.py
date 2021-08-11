n,L=map(int,input().split())
boxes=list(map(int,input().split()))
flag=True
center=0

for i in range(1,n):
    center+=boxes[i-1]
    if boxes[i-1]-L<center/i<boxes[i-1]+L:
        continue
    else:
        flag=False
        print("0")
        break 
if flag==True:
    print("1")


