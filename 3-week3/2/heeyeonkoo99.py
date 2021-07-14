#3주차-2

N=int(input())
T=[]
P=[]
dp=[]

def solution():
    for i in range(N):
        t,p=map(int,input().split())
        T.append(t)
        P.append(p)
        dp.append(p)
    dp.append(0)

    for i in range(N-1,-1,-1):
        if T[i]+i>N:
            dp[i]=dp[i+1]
        else:
            dp[i]=max(dp[i+1],P[i]+dp[(i+T[i])])
    print(dp[0])

solution()

#dp를 이용해서 N부터 시작하는 방법을 사용한다.=>표를 직접 그리면 이해가 잘된다..!