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
                if visited[r + plus][c + i] or visited[r + i][c + plus]:
                    return 0
            if not paper[r + i ][c + i]:
                return 0
            if visited[r + i ][c + i]:
                return 0
        except:
            return 0
        return 1  

    def check_range(r,c):
        for i in range(5):
            if check(r,c,i):
                continue
            return i - 1
        return i
    def toggle(r,c,i):
        for plus in range(i):
            if visited[r + plus][c + i]:
                visited[r + plus][c + i] = 0
            else:
                visited[r + plus][c + i] = i + 1
            if visited[r + i][c + plus]:
                visited[r + i][c + plus] = 0
            else:
                visited[r + i][c + plus] = i + 1
        if visited[r + i ][c + i]:
            visited[r + i ][c + i] = 0
        else:
            visited[r + i ][c + i] = i + 1
        # for plus in range(i):
        #     visited[r + plus][c + i] = 1 - visited[r + plus][c + i]
        #     visited[r + i][c + plus] = 1 - visited[r + i][c + plus]
        
        # visited[r + i ][c + i] = 1 - visited[r + i ][c + i]
    # bfs로 해야하나? -> 아냐 그러면 최소 100 * 100이 수두룩
    # dfs로 가지치기를 해야함. 더크면 바로 중단하게 
    # 쭉 돌면서 1인 곳을 메모부터 할까? 
    # 그리고 가능한 range도 ㅋㅋ
    # 오 이거 아이디어 좋은듯.  
    selects = []
    for plus in range(10):
        for tmp in range(plus):
            if paper[tmp][plus]:
                possible = check_range(tmp,plus)
                # 위치, 가능한 사각형 범위 0~4
                selects.append(([tmp,plus], possible))
            if paper[plus][tmp]:
                possible = check_range(plus,tmp)
                # 위치, 가능한 사각형 범위 0~4
                selects.append(([plus,tmp], possible))
        if paper[plus][plus]:
            possible = check_range(plus,plus)
            # 위치, 가능한 사각형 범위 0~4
            selects.append(([plus,plus], possible))
            

    goal = len(selects)

    def recur_find_best(idx):
        #print("=============",idx)
        #for v in visited:
        #    print(*v)
        #print(*used)
        #print("=============")
        global best_result
        if idx == goal:
            best_result = min(best_result, sum(used))
            return 
        elif sum(used) > best_result:
            return

        [r,c], possible = selects[idx]

        if visited[r][c]:
            recur_find_best(idx + 1)
            return 
        # 해당하는 범위를 visit 처리하고
        for p in range(possible, -1, -1):
            toggle(r,c,p)
        
        # 재귀를 보낸 후 빠지는 범위만큼만 visit 해제한다.
        for p in range(possible, -1, -1):
            if used[p] == 5:
                toggle(r,c,p)
                continue
            used[p] += 1
            recur_find_best(idx + 1)
            used[p] -= 1
            toggle(r,c,p)

    recur_find_best(0)
        


    print("##############",best_result)
    if best_result == MAX:
        return -1
    return best_result
#print(solve())

# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 0)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 4)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 5)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == -1)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 1 1 1 0 0 0 0 0 0
# 0 0 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 7)
# assert(solve('''1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1''') == 4)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0 0 0 0
# 0 1 1 1 1 1 0 0 0 0
# 0 0 1 1 1 1 0 0 0 0
# 0 0 1 1 1 1 0 0 0 0
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 0 1 1 1 1 1
# 0 1 1 1 0 1 1 1 1 1
# 0 0 0 0 0 1 1 1 1 1
# 0 0 0 0 0 1 1 1 1 1''') == 6)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 1 0 1 1 0 0 0
# 0 1 1 1 0 1 1 0 0 0
# 0 1 1 1 0 0 0 0 0 1''') == 5)
# assert(solve('''0 0 0 0 0 0 0 0 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 1 1 1 1 1 1 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 4)
# assert(solve('''1 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 1 1 0 1 1
# 1 1 0 1 1 1 1 0 1 1
# 1 1 0 1 1 0 0 1 1 1
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 1 1 0 1 1 1
# 1 1 1 1 1 1 0 0 1 1
# 0 0 0 1 1 1 0 0 1 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 13)
# assert(solve('''1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0''') == 6)
assert(solve('''1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0''') == 7)
