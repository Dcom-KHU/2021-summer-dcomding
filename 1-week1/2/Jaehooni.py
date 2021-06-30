directionLists = []
for i in range(1, 21):
    directionLists.append([])

directionLists[0].append(3)


def makeList(directionLists, number):
    startPoint = 1

    if (len(directionLists[number-2]) == 0):
        makeList(directionLists, number-1)

    for i in directionLists[number-2]:
        middlePoint = 6
        middlePoint -= startPoint
        middlePoint -= i

        directionLists[number-1].append(middlePoint)
        directionLists[number-1].append(i)

        startPoint = i


def calc(directionLists, number):
    sum = 0
    for i in range(0, number):
        for j in directionLists[i]:
            sum += j

    return sum


a = int(input())

makeList(directionLists, a)
print(calc(directionLists, a))
