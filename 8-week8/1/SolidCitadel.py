def distinguish(p1, p2, count):
    while count < 2 and p1 < p2:
        if word[p1] != word[p2]:
            count = min(distinguish(p1+1, p2, count+1), distinguish(p1, p2-1, count+1))
            break
        else:
            p1 += 1
            p2 -= 1
    return count

word = input()
print(distinguish(0, len(word)-1, 0))
