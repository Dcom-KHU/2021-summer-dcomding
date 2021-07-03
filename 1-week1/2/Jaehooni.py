directionLists = []
sumList = []

for i in range(1, 21):
    directionLists.append([])
    sumList.append(0)

directionLists[0].append(3)
sumList[0] = 3


def makeList(directionLists, number):
    startPoint = 1

    if (number == 1):
        pass

    else:
        if (len(directionLists[number-2]) == 0):
            makeList(directionLists, number-1)

        for i in directionLists[number-2]:
            middlePoint = 6 - (startPoint + i)

            directionLists[number-1].append(middlePoint)
            directionLists[number-1].append(i)
            sumList[number-1] += (middlePoint + i)

            startPoint = i


def calc(number):
    if (number == 1):
        return 3

    return sumList[number - 1] + calc(number-1)


a = int(input())

makeList(directionLists, a)
print(calc(a))
