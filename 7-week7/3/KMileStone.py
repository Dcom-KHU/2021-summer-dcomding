n = int(input())
cookies = list(map(int, input().split()))


max_cookie = 0

# if n == 1, you cannot distribute cookie
if n > 1:
    for b in range(n-1):
        a = b
        c = b+1
        brother = cookies[a]
        sister = cookies[c]

        while c < n:
            # if brother == sister, update max and a-- c++
            if brother == sister:
                if brother > max_cookie:
                    max_cookie = brother

                if a > 0 and c < n-1:
                    a -= 1
                    brother += cookies[a]
                    c += 1
                    sister += cookies[c]
                else:
                    break

            # if brother > sister, c++
            elif brother > sister:
                if c < n-1:
                    c += 1
                    sister += cookies[c]
                else:
                    break

            # if brother < sister, a--
            elif brother < sister:
                if a > 0:
                    a -= 1
                    brother += cookies[a]
                else:
                    break


print(max_cookie)
