def mat(sc, ind): #recursive function
    if sc[ind] == '(':
        if sc[ind+1] == ')': #if the next one matches a pair,
            sc.remove(sc[ind+1]) #remove the pair from string
            sc.remove(sc[ind])
            return True #and return True
        else: #if the next one does not match,
            mat(sc, ind+1) #call this function again from the 'next' index
            if sc[ind+1] == ')': #after all the recursion, if it matches,
                sc.remove(sc[ind+1]) #do the same thing
                sc.remove(sc[ind])
                return True
    elif sc[ind] == '{':
        if sc[ind+1] == '}':
            sc.remove(sc[ind+1])
            sc.remove(sc[ind])
            return True
        else:
            mat(sc, ind+1)
            if sc[ind+1] == '}':
                sc.remove(sc[ind+1])
                sc.remove(sc[ind])
                return True
    elif sc[ind] == '[':
        if sc[ind+1] == ']':
            sc.remove(sc[ind+1])
            sc.remove(sc[ind])
            return True
        else:
            mat(sc, ind+1)
            if sc[ind+1] == ']':
                sc.remove(sc[ind+1])
                sc.remove(sc[ind])
                return True
    else: #if match fails,
        return False #return False
    
s = list(input(""))
count = 0

for i in range(len(s)): #number of rotation are bound to length of s
    s.append(s[0])
    s.remove(s[0])

    sc = s[:] #copy string for deleting elements
    lc = len(sc) #limiting verification index

    complete = True #initialising complete flag

    while sc: #start verifying for a single rotation case
        if not mat(sc, 0): #if match finding function returns False (match finding failed)
            complete = False #abort the complete flag
            break #escape the while loop

    if complete: #if this rotation survived from while loop with complete flag,
        count += 1 #count this rotation

print(count)