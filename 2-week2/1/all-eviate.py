b = list(map(int, input("").split()))

#check bits in characters for decimal conversion
c1 = str((b[2]+b[4]+b[6]+b[8]+b[10]+b[12]+b[14]+b[0])%2)
c2 = str((b[2]+b[5]+b[6]+b[9]+b[10]+b[13]+b[14]+b[1])%2)
c3 = str((b[4]+b[5]+b[6]+b[11]+b[12]+b[13]+b[14]+b[3])%2)
c4 = str((b[8]+b[9]+b[10]+b[11]+b[12]+b[13]+b[14]+b[7])%2)

#convert check bits into decimal
checkbin = '0b'+c4+c3+c2+c1
check = int(checkbin, 2)

#if check bit is not 0, flip the faulty bit
if check != 0:
    b[check-1] = (b[check-1]+1) % 2

#convert fixed binary into decimal
n = int('0b'+str(b[14])+str(b[13])+str(b[12])+str(b[11])+str(b[10])+str(b[9])+str(b[8])+str(b[6])+str(b[5])+str(b[4])+str(b[2]), 2)
print(n)