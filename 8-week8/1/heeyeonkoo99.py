def check(left,right):
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True

def twopointer(left,right):
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            if check(left+1,right) or check(left,right-1): #그 전후 원소들은 볼필요가 없다 이미 같으니까!
                return 1
            return 2
        return 0
T = int(input()) 
for _ in range(T): 
    s = input() 
    print(twopointer(0, len(s)-1))

#Review) 투포인터 알고리즘 사용하기!