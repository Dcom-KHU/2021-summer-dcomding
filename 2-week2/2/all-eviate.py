s = list(input(""))
count = 0
l = len(s)

if l % 2 == 1: #if length is not even, print 0
    print(0)
else:
    for i in range(l): #number of rotation are bound to length of s
        s.append(s[0])
        s.remove(s[0])

        s = s[:] #copy string for deleting elements
        stack = [] #initialising stack
        complete = True #initialising complete flag

        for a in range(0, l):
            if not any(stack): #if stack is empty,
                if s[a] == ']' or s[a] == '}' or s[a] == ')': #check if the element is closing
                    complete = False #if it is, break from this rotation
                    break
                else:
                    stack.append(s[a])
            else: #if stack is not empty,
                if s[a] == ']' and stack[-1] == '[': #see if it can pop
                    stack.pop()
                elif s[a] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[a] == ')' and stack[-1] == '(':
                    stack.pop()
                else: #if it cannot, add current element to the stack
                    stack.append(s[a])
        if any(stack): #if stack is empty in the end, this rotation is valid
            complete = False

        if complete: #if this rotation survived from while loop with complete flag,
            count += 1 #count this rotation

    print(count)