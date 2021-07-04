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
        mid = lc // 2 #start searching pairs from the middle
        
        if sc[mid] == '(':
            mp = mid + 1 #searching for matcing pair in odd indeces
            if sc[mp] == ')': #if middle pair matches,
                sc.remove(sc[mp]) #remove the pair
                sc.remove(sc[mid])
                lc -= 2 #deduct the length by 2
                pair = True #raise flag to continue verification
                break
        elif sc[mid] == '{':
            mp = mid + 1
            if sc[mp] == '}':
                sc.remove(sc[mp])
                sc.remove(sc[mid])
                lc -= 2
                pair = True
                break
        elif sc[mid] == '[':
            mp = mid + 1
            if sc[mp] == ']':
                sc.remove(sc[mp])
                sc.remove(sc[mid])
                lc -= 2
                pair = True
                break
        else: #if the middle point of this rotation does not start with opening, it's wrong.
            complete = False
            break

        if pair:
            continue
        else: #if the middle pair does not match, it's wrong
            complete = False
            break
    if complete: #if this rotation survived while loop with complete flag, count this rotation
        count += 1
print(count)