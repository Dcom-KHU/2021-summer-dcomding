# C1 : XOR(D1, D2, D4, D5, D7, D9, D11, P1)
# C2 : XOR(D1, D3, D4, D6, D7, D10, D11, P2)
# C3 : XOR(D2, D3, D4, D8, D9, D10, D11, P3)
# C4 : XOR(D5, D6, D7, D8, D9, D10, D11, P4)
B = list(map(int, input().split()))
C1 = (B[2]^B[4]^B[6]^B[8]^B[10]^B[12]^B[14]^B[0])
C2 = (B[2]^B[5]^B[6]^B[9]^B[10]^B[13]^B[14]^B[1])
C3 = (B[4]^B[5]^B[6]^B[11]^B[12]^B[13]^B[14]^B[3])
C4 = (B[8]^B[9]^B[10]^B[11]^B[12]^B[13]^B[14]^B[7])
check = ''.join(map(str, [C4,C3,C2,C1]))
error = int(check, base=2)
result = []
cnt=0
if error != 0:
    B[error-1] = B[error-1] ^ 1
for i in range(15):
    if 2**cnt-1 == i:
        cnt+=1
        continue
    else:
        result.append(str(B[i]))
print(int(''.join(result[::-1]),base=2))