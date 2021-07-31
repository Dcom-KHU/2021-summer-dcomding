s = input()

ns = s[0]
for c in s:
    if c != ns[-1]:
        ns += c

print(len(ns)//2)
