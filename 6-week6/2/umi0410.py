_, _ = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
whole = set()
for n in A:
    whole.add(n)
for n in B:
    whole.add(n)

answer = len(whole)
for n in whole:
    if n in A and n in B:
        answer -= 1

print(answer)