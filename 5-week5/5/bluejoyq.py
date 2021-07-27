import sys
input = sys.stdin.readline
def solution():
    # 알파벳 하나 하나를 가지는 dictonary 중첩으로 푼다.
    # 만약 dict[char]의 len이 1이라면 자동완성이 되는걸로 쳐서 count를 하지 않는다.
    
    n = int(input())
    words = [0] * n
    
    # root에 tmp를 추가해 시작 알파벳이 다 같은 경우여도 count가 1은 나오게 해줘서
    # 첫글자는 자동완성이 안되는 것처럼 했다.
    root = {}
    root[""] = 0
    
    
    for i in range(n):
        # 단어를 입력받고
        words[i] = input().rstrip()
        cur = root
        # 각 단어의 글자마다 dict 안을 들어간다.
        for char in words[i]:
            try:
                cur =  cur[char]
            except:
                cur[char] = {}
                cur = cur[char]
        # 해당 단어에서 끝나는 경우와 그 이상으로 이어지는 경우 거르기 위해 tmp 추가
        cur[""] = 0
    
    result = ""
    # 각 단어로 쭉 파고 들어가면서 count 한다.
    for i in range(n):
        count = 0
        cur = root
        for char in words[i]:
            if len(cur) != 1:
                count += 1
            cur =  cur[char]
        
        result += str(count) + "\n"
    
    print(result)

solution()