s = input()
ch = s[0]
count = 1

for _, c in enumerate(s):
    if (ch != c):
        ch = c
        count += 1
   
print(count//2)
    

