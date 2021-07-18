def solve(n,t,m,timetable):
    answer=0
    crewtime=[int(time[0])*60+ int(time[1])for time in timetable]
    crewtime.sort()
    
    bustime=[9*60+ t*i for i in range(n)]
    
    i=0
    for tm in bustime:
        cnt=0
        while cnt<m and i<len(crewtime) and crewtime[i]<=tm:
            i+=1
            cnt+=1
        if cnt<m:
            answer=tm
            
        else:
            answer=crewtime[i-1]-1
    return str(answer//60)+" "+str(answer%60)

n,t,m,k=map(int,input().split())
table=[]
for i in range(k):
    a,b=map(int,input().split())
    table.append([a,b])
    
print(solve(n,t,m,table))