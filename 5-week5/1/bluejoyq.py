def solve():
    s = input()
    lst = s[0]
    result = 1
    for cur in s[1:]:
        if lst != cur:
            lst = cur
            result +=1
    print(result // 2)
    # 0으로 이루어진 블록과 1로 이루어진 블록의 개수를 센다
    # 둘 중 작은 것을 리턴
    # O(N)으로 가능. 더 줄이는 방법은?
    
    # 블록의 개수 / 2 하면 된다. 어차피 둘은 차이나봐야 최대 1 차이나므로
    # 최솟값을 찾으려면 // 연산으로 나머지를 버리면 된다.
solve()