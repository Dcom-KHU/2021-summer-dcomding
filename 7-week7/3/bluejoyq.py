def solution():
    # 2000 * 500은 백만.
    N = int(input())
    cookies = list(map(int, input().split()))
    
    # i는 경계선으로 i를 꼭 포함해야한다.
    
    result = 0
    for i in range(N - 1):
        boy = cookies[i]
        girl = cookies[i+1]
        boy_left = i
        girl_right = i + 1
        while not (boy_left == 0 and girl_right == N - 1):
            if boy == girl:
                result = max(boy, result )
                if boy_left == 0:
                    girl_right += 1
                    girl += cookies[girl_right]
                else:
                    boy_left -= 1
                    boy += cookies[boy_left]
            elif boy > girl:
                if girl_right == N- 1:
                    break
                girl_right += 1
                girl += cookies[girl_right]
            elif boy < girl:
                if boy_left == 0:
                    break
                boy_left -= 1
                boy += cookies[boy_left]
        if boy == girl:
            result = max(boy, result )
    return result
print(solution())
                