import sys
sys.setrecursionlimit(100000)
MAX = sys.maxsize
def solve(datas = None):
    N = 10
    if datas == None:
        paper = [list(map(int, input().split())) for i in range(N)]
    else:
        paper = [list(map(int,tmp.split())) for tmp in datas.split("\n")]
    used = [0] * 5
    visited = [[0] * N for i in range(N)]
    def check(r,c,i):
        
        try:
            for plus in range(i):
                if not paper[r + plus][c + i] or not paper[r + i][c + plus]:
                    return 0
            
            if not paper[r + i ][c + i]:
                return 0
        except:
            return 0
        return 1  
        '''
        try:
            for rr in range(r, r + i + 1):
                for cc in range(c, c + i + 1):
                    if not paper[rr][cc]:
                        return 0
            return 1
        except:
            return 0
        '''
    def toggle(r,c,i):
        for plus in range(i):
            visited[r + plus][c + i] = 1 - visited[r + plus][c + i]
            visited[r + i][c + plus] = 1 - visited[r + i][c + plus]
        
        visited[r + i ][c + i] = 1 - visited[r + i ][c + i]
        '''
        for rr in range(r, r + i + 1):
            for cc in range(c, c + i + 1):
                visited[rr][cc] = 1 - visited[rr][cc]
        '''

    def do_something(r,c):
        
        result = MAX
        for i in range(4):
            if not check(r,c,i):
                i -= 1
                break

        for tmp in range(i, -1, -1):
            toggle(r,c,tmp)
            
        for tmp in range(i, -1, -1):
            if used[tmp] == 5:
                continue

            used[tmp] += 1
            result = min(result ,find_best(r,c  + 1))
            used[tmp] -= 1
            toggle(r,c,tmp)
            
        return result
    def find_best(start_r, start_c):
        
        
        r= start_r
        
        for c in range(start_c):
            if not paper[r][c] or visited[r][c]:
                continue
            return do_something(r,c)
        for r in range(N):
            for c in range(N):
                if not paper[r][c] or visited[r][c]:
                    continue
                return do_something(r,c)
        return sum(used)

    # dfs로 가지치기를 해야함.   
    # 쭉 돌면서 1인 곳을 메모부터 할까? 
    # 그리고 가능한 range도 ㅋㅋ
    # 오 이거 아이디어 좋은듯.  
    findings = []
    for r in range(N):
        for c in range(N):
            if not paper[r][c]:
                continue

    print("##############",real_result)
    if real_result == MAX:
        return -1
    return real_result
#print(solve())

assert(solve('''0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == 0)
assert(solve('''0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == 4)
assert(solve('''0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == 5)
assert(solve('''0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == -1)
assert(solve('''0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == 7)
assert(solve('''1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1''') == 4)
assert(solve('''0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1''') == 6)
assert(solve('''0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 0 0 0 0 1''') == 5)