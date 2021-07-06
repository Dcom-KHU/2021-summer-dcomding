B = list(map(int, input().split()))


# C : [C4, C3, C2, C1]
C = ['null', 'null', 'null', 'null']
C[0] = str(B[8] ^ B[9] ^ B[10] ^ B[11] ^ B[12] ^ B[13] ^ B[14] ^ B[7])
C[1] = str(B[4] ^ B[5] ^ B[6] ^ B[11] ^ B[12] ^ B[13] ^ B[14] ^ B[3])
C[2] = str(B[2] ^ B[5] ^ B[6] ^ B[9] ^ B[10] ^ B[13] ^ B[14] ^ B[1])
C[3] = str(B[2] ^ B[4] ^ B[6] ^ B[8] ^ B[10] ^ B[12] ^ B[14] ^ B[0])

# bin * 4 -> int
C = int(''.join(C), 2)


# index of D : [D11, D10, D9, ..., D1]
idx_D = [14, 13, 12, 11, 10, 9, 8, 6, 5, 4, 2]

# extract and correct D by index, bin * 11 -> int
D = int(''.join(str(B[i]) if i != C-1 else str(B[i] ^ 1) for i in idx_D), 2)

print(D)
