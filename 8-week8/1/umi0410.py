s = input()
has_diff = False
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        has_diff = True
        break
if not has_diff:
    print(0)
else:
    # 하나라도 전체가 같은 경우가 있는지 체크
    for i in range(len(s)):
        _s = s[:i] + s[i+1:]
        has_diff = False
        # 하나라도 다른지 체크
        for j in range(len(_s)//2):
            if _s[j] != _s[j - 1]:
                has_diff = True
                break
        # 모두 같은 애가 하나라도 있는지 체크
        if not has_diff:
            break
    if not has_diff:
        print(1)
    else:
        print(2)

