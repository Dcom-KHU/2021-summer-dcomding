paper = []
for i in range(10):
    paper.append(list(map(int, input().split())))


def is_square(x, y, side=2):
    for i in range(side):
        for j in range(side):
            if x+i >= 10 or y+j >= 10 or paper[x+i][y+j] == 0:
                return False
    return True

min_paper = float('inf')
count = [0 for i in range(5)]

def dfs():
    global min_paper

    # if 1 is not exist, update min
    if sum(map(sum, paper)) == 0:
        if sum(count) < min_paper:
            min_paper = sum(count)
        return True

    # if current used >= min, no more branch
    elif sum(count) >= min_paper:
        return False

    # else, more branch
    else:
        # find 1
        for x in range(10):
            for y in range(10):
                if paper[x][y] == 1:
                    # loop for side of square
                    for s in range(5, 0, -1):
                        # if square available and (x, y) is top-left of s-square
                        if count[s-1] < 5 and is_square(x, y, s):
                            # remove square
                            for i in range(s):
                                for j in range(s):
                                    paper[x+i][y+j] = 0
                            count[s-1] += 1

                            # branch with removed state
                            dfs()

                            # restore square
                            for i in range(s):
                                for j in range(s):
                                    paper[x+i][y+j] = 1
                            count[s-1] -= 1

                    return


dfs()

if min_paper == float('inf'):
    print(-1)
else:
    print(min_paper)
