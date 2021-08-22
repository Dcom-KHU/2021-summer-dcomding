word = input()


count = 0
left = 0
right = len(word)-1

while left < right:
    if word[left] == word[right]:
        left += 1
        right -= 1
    elif count < 2:
        count += 1

        # if left letter is obstacle
        if word[left+1] == word[right]:
            left += 1

        # if right letter is obstacle
        elif word[left] == word[right-1]:
            right -= 1

        # if different at all
        else:
            count = 2
            break


print(count)
