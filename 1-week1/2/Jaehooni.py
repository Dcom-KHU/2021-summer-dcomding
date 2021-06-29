def empty(list):
    if (len(list) == 0):
        return True

    else:
        return False


def chooseDirection(directionList):
    direction = [1, 2, 3]
    a, b = directionList[0], directionList[1]
    direction.remove(a)
    direction.remove(b)

    return direction[0]


def makeDirectionList(DirectionListList, number):

    previousDirectionList = DirectionListList[number - 2]
    currentDirectionList = DirectionListList[number - 1]

    if (empty(previousDirectionList)):
        makeDirectionList(DirectionListList, number - 1)

    for direction in previousDirectionList:
        start, end = direction[0], direction[1]
        stop = chooseDirection(direction)
        currentDirectionList.append([start, stop])
        currentDirectionList.append([stop, end])


def hanoiSum(directionListList, number):
    if (number == 0):
        return 0

    elif (number == 1):
        return 3

    else:
        sum = 0

        if (empty(directionListList[number-1])):
            makeDirectionList(directionListList, number)

        for direction in directionListList[number-1]:
            sum += direction[1]

        return sum + hanoiSum(directionListList, number-1)


directionLists = [[[1, 3]]]

for i in range(1, 20):
    directionLists.append([])


inputNumber = int(input())


print(hanoiSum(directionLists, inputNumber))
