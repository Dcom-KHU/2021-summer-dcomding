#일찍 시작하는 순으로 정렬 : 반례 존재 (2,3), (4,5), (1,10)
#회의 길이가 짧은 순으로 정렬 : 반례 존재(2,5),(4,6),(5,9)
#일찍 끝나는 순으로 정렬 : 가능
#끝나는 시간이 같은 경우 시작하는 시간이 더 빠른 순으로 정렬
#매회마다 가장 최적이라 생각되는 답을 선택하는 greedy 알고리즘 사용
#https://docs.python.org/ko/3/howto/sorting.html 참고
from operator import itemgetter
n = int(input())
times = []
answer = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    times.append(temp)

times.sort(key=itemgetter(1,0)) # 끝나는 시간->시작 시간 기준으로 정렬
last_end = 0
for start, end in times:
    if start >= last_end:
        last_end = end
        answer += 1
print(answer)