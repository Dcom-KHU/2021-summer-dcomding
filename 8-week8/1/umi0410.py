import sys
input = sys.stdin.readline

def check(s, diff_cnt):
    if diff_cnt == 2:
        return 2
    else:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return min(check(s[:i] + s[i+1:], diff_cnt + 1),
                           check(s[:len(s)-i-1] + s[len(s)-i:], diff_cnt + 1))
        return diff_cnt

for _ in range(int(input())):
    s = input().strip()
    print(check(s, 0))

