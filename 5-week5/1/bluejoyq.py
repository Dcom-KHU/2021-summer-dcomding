def solve():
    s = input()
    # 0으로 이루어진 블록과 1로 이루어진 블록의 개수를 센다
    # 둘 중 작은 것을 리턴
    # O(N)으로 가능. 더 줄이는 방법은?
    result ={"0":0, "1":0}
    lst = s[0]
    result[lst]= 1
    for cur in s[1:]:
        if lst == cur:
            continue
        lst = cur
        result[lst] += 1
    print(min(result.values()))
solve()