def solve():
    input()
    a_values = set(map(int, input().split()))
    b_values = set(map(int, input().split()))
    
    print(len((b_values | a_values) - (a_values & b_values)))
solve()