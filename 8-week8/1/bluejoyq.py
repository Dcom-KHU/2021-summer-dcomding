def solve(word ):
    
    N = len(word)
    jumped = 0
    left_jump = 0
    right_jump= 0
    for i in range(N // 2):
        left = i + left_jump
        right = N - 1 - i + right_jump
        if word[left] == word[right]:
            continue
        
        if jumped:
            return 2
        
        if word[left + 1] == word[right]:
            left_jump = 1
            jumped = 1
        elif word[left] == word[right - 1]:
            right_jump = -1
            jumped = 1
        else:
            return 2
    
    if jumped:
        return 1
    return 0
word = input()
print(solve(word))
'''
assert(solve("abba") == 0)
assert(solve("summuus") == 1)
assert(solve("xabba") == 1)
assert(solve("xabbay") == 2)
assert(solve("comcom") == 2)
assert(solve("comwwmoc") == 0)
assert(solve("comwwtmoc") == 1)
'''


 