import sys
sys.setrecursionlimit(100000)
MAX = sys.maxsize



def solve(datas = None):
    global best_result
    N = 10
    if datas == None:
        paper = [list(map(int, input().split())) for i in range(N)]
    else:
        paper = [list(map(int,tmp.split())) for tmp in datas.split("\n")]
    
    used = [0] * 5
    visited = [[0] * N for i in range(N)]
    best_result = MAX

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

    def check_range(r,c):
        for i in range(4):
            if check(r,c,i):
                continue
            return i - 1

    def toggle(r,c,i):
        for plus in range(i):
            visited[r + plus][c + i] = 1 - visited[r + plus][c + i]
            visited[r + i][c + plus] = 1 - visited[r + i][c + plus]
        
        visited[r + i ][c + i] = 1 - visited[r + i ][c + i]


    
    # bfs로 해야하나? -> 아냐 그러면 최소 100 * 100이 수두룩
    # dfs로 가지치기를 해야함. 더크면 바로 중단하게 
    # 쭉 돌면서 1인 곳을 메모부터 할까? 
    # 그리고 가능한 range도 ㅋㅋ
    # 오 이거 아이디어 좋은듯.  
    selects = []
    for r in range(N):
        for c in range(N):
            if not paper[r][c]:
                continue
            possible = check_range(r,c)
            # 위치, 가능한 사각형 범위 0~4
            selects.append(([r,c], possible))

    goal = len(selects)
    # 인자 하나 더주고 가지치기 하는게 더 나음
    def recur_find_best(idx):
        global best_result
        if idx == goal:
            best_result = min(best_result, sum(used))
            return 
        elif sum(used) > best_result:
            return

        [r,c], possible = selects[idx]

        if visited[r][c]:
            recur_find_best(idx + 1)
        
        for tmp in range(possible):
            toggle(r,c,tmp)
        for p in range(possible, -1, -1):
            if used[p] == 4:
                continue
            recur_find_best(idx)
            toggle(r,c,p)

    recur_find_best(0)
        


    #print("##############",best_result)
    if best_result == MAX:
        return -1
    return best_result
print(solve())

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