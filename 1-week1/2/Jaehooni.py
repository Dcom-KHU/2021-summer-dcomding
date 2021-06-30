directionLists = []
sumList = []
for i in range(1, 21):
    directionLists.append([])

directionLists[0].append(3)
sumList.append(3)


def calc(directionLists, number):
    sum = 0
    startPoint = 1

    if (len(directionLists[number-2]) == 0):
        calc(directionLists, number-1)

    for i in directionLists[number-2]:
        middlePoint = 6
        middlePoint -= startPoint
        middlePoint -= i

        directionLists[number-1].append(middlePoint)
        directionLists[number-1].append(i)

        sum += middlePoint
        sum += i

        startPoint = i

    sumList.append(sum)


def printSum(number):
    sum = 0
    for i in range(0, number):
        sum += sumList[i]

    print(sum)


a = int(input())
calc(directionLists, a)
printSum(a)
