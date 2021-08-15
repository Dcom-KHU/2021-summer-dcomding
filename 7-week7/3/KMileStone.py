n = int(input())
cookies = list(map(int, input().split()))


a = 0
b = 0
c = 1
brother = cookies[a]
sister = cookies[c]
max_cookie = 0

while c < n:
    # if brother == sister, update max and c++
    if brother == sister:
        max_cookie = brother
        c += 1
        if c < n:
            sister += cookies[c]
        else:
            break

    # if brother > sister, a++
    elif brother > sister:
        brother -= cookies[a]
        a += 1

        # if a > b, shift b together
        if a > b:
            b += 1
            brother += cookies[b]
            sister -= cookies[b]

            # if b == c, shift c together
            if b == c:
                c += 1
                if c < n:
                    sister += cookies[c]
                else:
                    break

    # if brother < sister, b++
    elif brother < sister:
        b += 1
        brother += cookies[b]
        sister -= cookies[b]

        # if b == c, shift c together
        if b == c:
            c += 1
            if c < n:
                sister += cookies[c]
            else:
                break


print(max_cookie)
