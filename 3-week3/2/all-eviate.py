n = int(input(""))

wage = [0]*n
comm = []

for a in range(n):
    comm.append(tuple(map(int, input("").split()))) #t와 k를 튜플로 저장

for day in range(0,n):

    if day + comm[day][0] <= n: #방햑을 넘기지 않는다면

        wage[day] = comm[day][1] #day날에 일한 보수를 저장

        for bef in range(0, day+1): #첫날부터 day 이전의 날, bef들 중

            if bef + comm[bef][0] <= day: #그때 받은 외주가 겹치지 않는다면

                wage[day] = max(wage[day], wage[bef]+comm[day][1]) #보수를 합산

print(max(wage)) 