s = input()


# string : depth of big, mid, small bracket
# [](){} : 1 0 0 -> 0 0 0 -> 0 0 1 -> 0 0 0 -> 0 1 0 -> 0 0 0   -> valid
# [(())] : 1 0 0 -> 1 0 1 -> 1 0 2 -> 1 0 1 -> 1 0 0 -> 0 0 0   -> valid
# {(])[} : 0 1 0 -> 0 1 1 -> -1 1 1                             -> invalid : started with ]
# [(){}  : 1 0 0 -> 1 0 1 -> 1 0 0 -> 1 1 0 -> 1 0 0            -> invalid : unclosed
# ([{)}] : 0 0 1 -> 1 0 1 -> 1 1 1 -> 1 1 0 -> 1 0 0 -> 0 0 0   -> invalid : impossible form with primitive () {} []

count = 0

for i in range(len(s)):
    # L-shift
    shifted = s[i:] + s[:i]

    big = 0
    mid = 0
    small = 0
    valid = True

    # (A) {A} [A] AB should have primitives () {} []
    if "()" not in shifted and "{}" not in shifted and "[]" not in shifted:
        valid = False

    else:
        # check depth of shifted
        for c in shifted:
            if c == '[':
                big += 1
            elif c == ']':
                big -= 1
            elif c == '{':
                mid += 1
            elif c == '}':
                mid -= 1
            elif c == '(':
                small += 1
            elif c == ')':
                small -= 1

            # if depth < 0, phrase started with ] } )
            if big < 0 or mid < 0 or small < 0:
                valid = False
                break

    # if depth > 0 after loop, phrase unclosed
    # if depth == 0 after loop, valid string
    if valid == True and big == 0 and mid == 0 and small == 0:
        count += 1

print(count)
