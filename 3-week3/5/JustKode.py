n = int(input())
heights = list(map(int, input().split()))
tree = [0] * (4 * n)

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        init(arr, tree, node * 2, start, mid)
        init(arr, tree, node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] if arr[tree[node * 2]] < arr[tree[node * 2 + 1]] else tree[node * 2 + 1]

def find(arr, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    i = find(arr, tree, node * 2, start, mid, left, right)
    j = find(arr, tree, node * 2 + 1, mid + 1, end, left, right)

    if i == -1:
        return j
    elif j == -1:
        return i
    else:
        return i if arr[i] < arr[j] else j

def large(arr, tree, start, end):
    m = find(arr, tree, 1, 0, n - 1, start, end)
    area = (end - start + 1) * arr[m]

    if start <= m - 1:
        temp = large(arr, tree, start, m - 1)
        area = max(area, temp)

    if m + 1 <= end:
        temp = large(arr, tree, m + 1, end)
        area = max(area, temp)
    
    return area

init(heights, tree, 1, 0, n - 1)
print(large(heights, tree, 0, n - 1))