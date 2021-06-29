maxi, mini = -10**9, 10**9
def fn(num, i, a, b, c, d):
    global maxi, mini
    if not a+b+c+d:
        maxi, mini = max(maxi, num), min(mini, num)
    else:
        if a:
            fn(num+arr[i], i+1, a-1, b, c, d)
        if b:
            fn(num-arr[i], i+1, a, b-1, c, d)
        if c:
            fn(num*arr[i], i+1, a, b, c-1, d)
        if d:
            fn(int(num/arr[i]),i+1, a, b, c, d-1)

n = int(input())
arr = list(map(int, input().split()))
fn(arr[0], 1, *map(int, input().split()))
print(maxi)
print(mini)
