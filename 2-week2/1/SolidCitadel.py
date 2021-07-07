B = list(map(int, input().split()))
C = [str(sum([B[i] for i in [-1-p-d for p in range(0, 15, 2**(x+1)) for d in range(2**x)][0:7]] + [B[2**x-1]])%2) for x in range(4)]
error = int('0b'+''.join(C[::-1]), base=0)
if error:
    B[error-1] = 1 - B[error-1]
print(int('0b'+''.join([str(B[i-1]) for i in range(1, 16) if i not in [2**x for x in range(4)]][::-1]), base=0))
