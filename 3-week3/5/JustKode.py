import sys
import math
sys.setrecursionlimit(10**9)

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
tree = [0] * (pow(2, math.ceil(math.log(n,2)) + 1))

def init(node, start, end):
    global arr, tree
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] if arr[tree[node * 2]] < arr[tree[node * 2 + 1]] else tree[node * 2 + 1]


def find(node, start, end, left, right):
    global arr, tree
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    i = find(node * 2, start, mid, left, right)
    j = find(node * 2 + 1, mid + 1, end, left, right)

    if i == -1:
        return j
    elif j == -1:
        return i
    else:
        return i if arr[i] < arr[j] else j


def large(start, end):
    global arr, tree
    m = find(1, 0, n - 1, start, end)
    area = (end - start + 1) * arr[m]

    if start <= m - 1:
        temp = large(start, m - 1)
        area = max(area, temp)

    if m + 1 <= end:
        temp = large(m + 1, end)
        area = max(area, temp)
    
    return area

init(1, 0, n - 1)
print(large(0, n - 1))