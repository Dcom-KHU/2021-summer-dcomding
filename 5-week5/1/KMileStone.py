s = input()


# 000 11 00   : 2 0-group, 1 1-group -> need 1 flip
# 11 00 11 00 : 2 0-group, 2 1-group -> need 2 flip

count_0 = 0
count_1 = 0
prev = ''

# count groups
for arrow in s:
    if prev != '0' and arrow == '0':
        count_0 += 1
        prev = '0'
    elif prev != '1' and arrow == '1':
        count_1 += 1
        prev = '1'

# take min
print(min(count_0, count_1))
