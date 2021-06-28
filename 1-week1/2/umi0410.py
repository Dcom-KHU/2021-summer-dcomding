# 하노이

size = int(input())
# towels 의 값은 각 타워의 최고값을 의미한다.
# -1인 경우는 타워가 없는 경우
# e.g. [3, -1, -1]

# 나머지 한 칸의 인덱스 얻기
def get_rest_one(a, b):
    tmp = [0, 1, 2]
    tmp.remove(a)
    tmp.remove(b)
    return tmp[0]

# 현재 타워가 src에서 dest로 가고 싶음
# index로 계산하기 때문에 src=0인 경우 1번 타워에서 출발한다는 의미
def move(current_top_value, src, dest):
    if current_top_value == 1:
        return dest + 1
    else:
        return move(current_top_value-1, src, get_rest_one(src, dest)) + dest + 1 + move(current_top_value-1, get_rest_one(src, dest), dest)

print(move(size, 0, 2))