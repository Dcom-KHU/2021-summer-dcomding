import sys 
input = sys.stdin.readline
MAX_VAL = 120120
def solve():
    N = int(input())
    target = input().rstrip() 
    words_by_first_char = {}
    words = [0] * N
    for i in range(N):
        tmp = input().rstrip()
        words[i] = tmp
        try:
            words_by_first_char[tmp[0]].append(i)
        except:
            words_by_first_char[tmp[0]] = [i]
    M = len(target)
    
    cache = [[MAX_VAL] * (N) for i in range(M)]
    
    for nxt in words_by_first_char[target[0]]:
        cache[0][nxt] = [1,1]
    for i in range(1, M):
        cur_char = target[i]
        no_home = MAX_VAL
        for j in range(N):
            if cache[i - 1][j] == MAX_VAL:
                continue
            cur_idx, score = cache[i - 1][j]
            try:
                if cur_char != words[j][cur_idx]:
                    continue
                cache[i][j] = [cur_idx + 1, score]
            except:
                no_home = min(no_home, score)
        # 새로 단어를 찾아야하면.
        if no_home != MAX_VAL:
            for nxt in words_by_first_char[cur_char]:
                if cache[i][nxt] == MAX_VAL or cache[i][nxt][1] > no_home + 1:
                    cache[i][nxt] = [1,no_home + 1]
                
    result = MAX_VAL
    for i in range(N):
        lst = cache[M-1][i]
        if lst == MAX_VAL or lst[0] != len(words[i]):
            continue
        result = min(result, lst[1])

    if result == MAX_VAL:
        return -1
    return result
print(solve())