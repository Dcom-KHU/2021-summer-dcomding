# 풀이법이 떠오르지 않는다. 처음 보는 유형이다...
# 그냥 1번에서 시작해서 다 포함하는 경우
# 2번에서 시작해서 다 포함하는 경우 이렇게 다 세보면 효율성이 오바일까..? 최대 10만칸임...
# 약간 dp스럽게 전꺼를 바탕으로 생각하는 게 좋겠다.
# 전꺼를 없앤 대신 걔가 포함되어있으면 ㄱㅊ은 거니까.

def solution(gems):

    end = -1
    first_set = set()
    gems_set = set(gems)

    for i in range(len(gems)):
        gem = gems[i]
        gems_set.discard(gem)
        if len(gems_set) == 0:
            end = i
            break
    answers = [(end+1, 0, end)]
    products = gems[:end+1]
    for i in range(1, len(gems)):
        found, end, products = shop(gems, i, end, products)
        if not found:
            break
        length = end - i + 1
        if length == answers[0][0]:
            answers.append((length, i, end))
        elif length < answers[0][0]:
            answers = [(length, i, end)]

    # print(answers)
    answer = sorted(answers)[0]
    return [answer[1] + 1, answer[2] + 1]

# end 포함
def shop(gems, start, end, _current_products):
    before_product = gems[start-1]
    is_complete = False
    new_end = -1

    current_products = _current_products[1:]
    if before_product not in current_products:
        for i in range(end+1, len(gems)):
            current_products.append(gems[i])
            # 이전에 뺸 녀석을 찾은 경우
            if gems[i] == before_product:
                is_complete = True
                new_end = i
                break
    else:
        is_complete = True
        new_end = end
    return is_complete, new_end, current_products



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))