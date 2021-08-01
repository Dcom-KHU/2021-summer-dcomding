arrows=str(input())
one,zero=0,0

if arrows[0]=="1":
    zero+=1
else:
    one+=1
for i in range(0,len(arrows)-1):
    if arrows[i]!=arrows[i+1] and arrows[i+1]=="1":
        zero+=1
    elif arrows[i]!=arrows[i+1] and arrows[i+1]=="0":
        one+=1
    else:
        continue
print(min(one,zero))