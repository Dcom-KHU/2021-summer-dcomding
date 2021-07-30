chars = input()
chars += chars[0] # dummy
answer = 0
for i in range(1, len(chars) - 1):
    if chars[i] != chars[0] and chars[i] != chars[i + 1]:
        answer += 1
print(answer)