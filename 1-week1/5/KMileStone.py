n = int(input())
money = list(map(int, input().split()))


max_val = [0 for i in range(n)]

# recursive
def steal(val, idx, head):
    # head neighbor tail
    if not(head == 0 and idx == n-1):
        val += money[idx]

        # update max
        if val > max_val[head]:
            max_val[head] = val

            # steal more in non-neighbor
            for i in range(2, n-idx):
                steal(val, idx+i, head)

for i in range(n):
    steal(0, i, i)

print(max(max_val))
