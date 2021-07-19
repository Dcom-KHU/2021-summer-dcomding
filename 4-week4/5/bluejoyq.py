import sys
input = sys.stdin.readline
def solve():
    N = int(input())
    values = list(map(int,input().split()))
    
    tree = [0] * (N*2 + 1)
    result_str = ""
    result = 0
    for value in values:
        lo = 0
        hi = (N * 2)
        num = 0
        while lo <= hi:
            
            mid = (lo + hi) // 2
            #print(mid, tree)
            if tree[mid]:
                if tree[mid] < value: 
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                tree[mid] = value
                break
                
            num += 1
        result += num
        result_str += str(result) + "\n"
    print(result_str)
solve()