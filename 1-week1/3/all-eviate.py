n = int(input(""))
nums = input("").split()
for i in range(n):
    nums[i] = int(nums[i])
add, sub, mul, div = input("").split()
result_max = -1000000000
result_min = 1000000000

#asmd
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#asdm
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#amsd
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#amds
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#adsm
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#adms
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result

#samd
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#sadm
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#sdam
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#sdma
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#smad
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#smda
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result

#masd
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#mads
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#msad
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#msda
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#mdas
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#mdsa
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if muler > 0:
        result = result * nums[i]
        muler -= 1
    elif diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result

#dams
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#dasm
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#dmas
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#dmsa
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#dsam
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result
#dsma
adder = int(add)
suber = int(sub)
muler = int(mul)
diver = int(div)
result = nums[0]
for i in range(1, n):
    if diver > 0:
        if result >= 0:
            result = result//nums[i]
        else:
            result = -(-result//nums[i])
        diver -= 1
    elif suber > 0:
        result -= nums[i]
        suber -= 1
    elif muler > 0:
        result = result * nums[i]
        muler -= 1
    elif adder > 0:
        result += nums[i]
        adder -= 1
if result < result_min:
    result_min = result
if result > result_max:
    result_max = result

print(result_max)
print(result_min)