side_num = int(input())
value_list = list(map(int, input().split()))


def thief(side_num, current_list):
    value = 0
    max_value = 0
    if (side_num == 1):
        return current_list[0]

    elif (side_num == 2):
        return max(current_list[0], current_list[-1])

    else:
        for index in range(0, side_num):
            if (choose(index, current_list)):
                value = current_list[index] + thief(side_num-3, remove(index, current_list))
                # print(current_list[index], thief(side_num-3, remove(index, current_list)))
                # print(f'this value is {value}')

            if (value > max_value):
                # print(f'{value} is bigger than {max_value}!')
                max_value = value

    return max_value


def choose(index, current_list):
    length = len(current_list)
    if (index == length - 1):
        if (value_list[index] >= value_list[0] and value_list[index] >= value_list[index - 1]):
            # print(f'{value_list[index]} is bigger than {value_list[0]} and {value_list[index-1]}')
            return True

        else:
            # print(f'{value_list[index]} is not bigger than {value_list[0]} and {value_list[index-1]}')
            return False

    elif (index == 0):
        if (value_list[index] >= value_list[1] and value_list[index] >= value_list[-1]):
            # print(f'{value_list[index]} is bigger than {value_list[1]} and {value_list[-1]}')
            return True

        else:
            # print(f'{value_list[index]} is not bigger than {value_list[1]} and {value_list[-1]}')
            return False

    else:
        if (value_list[index] >= value_list[index-1] and value_list[index] >= value_list[index+1]):
            # print(f'{value_list[index]} is bigger than {value_list[index-1]} and {value_list[index+1]}')
            return True

        else:
            # print(f'{value_list[index]} is not bigger than {value_list[index-1]} and {value_list[index+1]}')
            return False


def remove(index, current_list):
    length = len(current_list)

    if (index == length - 1):
        # print(value_list[1:-2])
        return value_list[1:-2]

    elif (index == 0):
        # print(value_list[2:-1])
        return value_list[2:-1]

    else:
        # print(value_list[:index-1] + value_list[index+2:])
        return value_list[:index-1] + value_list[index+2:]


print(thief(side_num, value_list))