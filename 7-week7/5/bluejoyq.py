import sys
input = sys.stdin.readline
MAX= sys.maxsize
sys.setrecursionlimit(300000)
def solution():
    N = int(input())
    values = list(map(int, input().split()))
    nodes = {}
    for i in range(N - 1):
        a,b = map(int, input().split())
        try:
            nodes[a].append(b)
        except:
            nodes[a] = [b]
    cache = [0 for i in range(N )]
    def recur_find_min(cur, selected):
        try:
            
            # cur을 골랐다면
            if selected == 1:
                result = 0
                for nxt in nodes[cur]:
                    if not cache[nxt]:
                        cache[nxt] = recur_find_min(nxt, 0) 
                    result += cache[nxt]
                result += values[cur]
            else:
                tmp = 0
                result = MAX
                for nxt in nodes[cur]:
                    if not cache[nxt]:
                        cache[nxt] = recur_find_min(nxt, 0) 
                    tmp += cache[nxt]
                for nxt in nodes[cur]:
                    result = min(result, tmp - cache[nxt] + recur_find_min(nxt, 1))
                result = min(result, tmp + values[cur])
            return result 
        except:
            if selected == 1:
                return values[cur]
            return 0
    
    return min(recur_find_min(0, 0) , recur_find_min(0, 1))
print(solution())
