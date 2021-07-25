meeting=[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    meeting.append((a,b))
#print(meeting)-체크용

meeting=sorted(meeting,key=lambda a:a[0])
meeting=sorted(meeting,key=lambda a:a[1]) #끝나는 시간이 같을 경우를 생각해준다!

cnt, end=0,0

for a,b in meeting:
    if a>=end:
        cnt+=1
        end=b
print(cnt)
