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
        if left+1 < right and word[left+1] == word[right]:
            left += 1

        # if right letter is obstacle
        elif left < right-1 and word[left] == word[right-1]:
            right -= 1

        # if mid of even word
        elif right != len(word) // 2:
            break

        # if different at all
        else:
            count = 2
            break


print(count)
