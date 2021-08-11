n,L=map(int,input().split())
boxes=list(map(int,input().split()))
center=0
flag=True

for i in range(n-1,0,-1): # 그림의 위치를 떠올리면 순서대로 A,B,C,D...등이 있기에 뒤에서부터 돌린다.
    center+=boxes[i] 
    if boxes[i-1]-L<center/(n-i)<boxes[i-1]+L: # 그 바로 아래에 있는 box에 대해 보는것이다.
        continue
    else:
        flag=False
        break 
if flag==True:
    print("1")
else:
    print("0")
   
