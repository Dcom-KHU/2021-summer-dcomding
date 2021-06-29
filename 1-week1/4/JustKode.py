n, k = map(int, input().split())
stones = list(map(int, input().split()))

def can_work(people):
    global n, k, stones
    distence = 0
    for stone in stones:
        if stone < people:
            distence += 1
        else:
            distence = 0
        
        if distence >= k:
            return False
    return True


left = 1
right = n
max_people = 0

while left <= right:
    people = (left + right) // 2
    if can_work(people):
        left = people + 1
        max_people = max(max_people, people)
    else:
        right = people - 1

print(max_people)