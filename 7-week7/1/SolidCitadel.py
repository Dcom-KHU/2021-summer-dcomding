n, L = map(int, input().split())
C = list(map(int, input().split()))

x = C[-1]
try:
    for i in range(n-2, -1, -1):
        if x-L < C[i] < x+L:
            x = ((n-i-1)*x + C[i]) / (n-i)
        else:
            raise Exception
except:
    print("0")
else:
    print("1")
