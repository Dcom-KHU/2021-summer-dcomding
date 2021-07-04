s = list(input(""))
count = 0

for i in range(len(s)): #number of rotation are bound to length of s
    s.append(s[0])
    s.remove(s[0])

    sc = s[:] #copy string for deleting elements
    lc = len(sc) #limiting verification index

    complete = True #initialising complete flag

    while sc: #start verifying for a single rotation case
        pair = False #flag for finding a correct pair
        
        if sc[0] == '(':
            i = 1 #searching for matcing pair in odd indeces
            while i < lc:
                if sc[i] == ')': #if match is found,
                    sc.remove(sc[i]) #delete the closing match from copied string,
                    sc.remove(sc[0]) #and the opening one
                    lc -= 2 #deducting 2 in length
                    pair = True #pair is found,
                    break #exit while loop to find a new match
                i += 2 #increasing searching index by 2
        elif sc[0] == '{':
            i = 1
            while i < lc:
                if sc[i] == '}':
                    sc.remove(sc[i])
                    sc.remove(sc[0])
                    lc -= 2
                    pair = True
                    break
                i += 2
        elif sc[0] == '[':
            i = 1
            while i < lc:
                if sc[i] == ']':
                    sc.remove(sc[i])
                    sc.remove(sc[0])
                    lc -= 2
                    pair = True
                    break
                i += 2
        else: #if this rotation does not start with opening, it's wrong.
            complete = False
            break

        if pair:
            continue
        else: #if pair is not found in search above, it's wrong
            complete = False
            break
    if complete: #if this rotation survived while loop with complete flag, count this rotation
        count += 1
print(count)