s = list(map(int, list(input())))

answer = 0
switch = False
if s[0] == 0:   
    for i in range(len(s)):
        if s[i] == 1:
            switch = True
        elif switch:
            answer += 1
            switch = False
else:
    for i in range(len(s)):
        if s[i] == 0:
            switch = True
        elif switch:
            answer += 1
            switch = False
    
if switch:
    answer += 1
print(answer)