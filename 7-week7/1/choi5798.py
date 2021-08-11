n, m = map(int, input().split())
blocks = list(reversed(list(map(int, input().split()))))
stable = True
total = 0
for i in range(1, n):
    total += blocks[i-1]
    # print('{}번 박스의 구간: {} ~ {}'.format(n-i, blocks[i]-m, blocks[i]+m))
    # print('~{}번 박스의 중심범위: {}'.format(n-i+1, total/i))
    if blocks[i]-m < total / i < blocks[i]+m:
        pass
    else:
        stable = False
        break
if stable:
    print(1)
else:
    print(0)