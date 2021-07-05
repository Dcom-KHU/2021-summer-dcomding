from functools import reduce

# 역순으로 주어졌으니 다시 역순으로 치환해서 값을 받음
bit_list = list(map(int, input().split()))[::-1]

# 실제 계산할 때 쓰이지 않는 체크 비트들을 제외하기 위함
not_real_value = [-8, -4, -2, -1]

b1_bit = [bit_list[-3], bit_list[-5], bit_list[-7], bit_list[-9], bit_list[-11], bit_list[-13], bit_list[-15]]
b2_bit = [bit_list[-3], bit_list[-6], bit_list[-7], bit_list[-10], bit_list[-14], bit_list[-14], bit_list[-15]]
b3_bit = [bit_list[-5], bit_list[-6], bit_list[-7], bit_list[-12], bit_list[-13], bit_list[-14], bit_list[-15]]
b4_bit = [bit_list[-9], bit_list[-10], bit_list[-11], bit_list[-12], bit_list[-13], bit_list[-14], bit_list[-15]]

b1 = reduce(lambda x, y: x ^ y, b1_bit)
b2 = reduce(lambda x, y: x ^ y, b2_bit)
b3 = reduce(lambda x, y: x ^ y, b3_bit)
b4 = reduce(lambda x, y: x ^ y, b4_bit)

#print(b4, b3, b2, b1)
#print(bit_list[-8], bit_list[-4], bit_list[-2], bit_list[-1])


# 각 검증 비트들의 계산 요소들을 구함
c1_bit = [bit_list[-3], bit_list[-5], bit_list[-7], bit_list[-9], bit_list[-11], bit_list[-13], bit_list[-15], b1]#bit_list[-1]]
c2_bit = [bit_list[-3], bit_list[-6], bit_list[-7], bit_list[-10], bit_list[-14], bit_list[-14], bit_list[-15], b2]# bit_list[-2]]
c3_bit = [bit_list[-5], bit_list[-6], bit_list[-7], bit_list[-12], bit_list[-13], bit_list[-14], bit_list[-15], b3]#bit_list[-4]]
c4_bit = [bit_list[-9], bit_list[-10], bit_list[-11], bit_list[-12], bit_list[-13], bit_list[-14], bit_list[-15], b4]#bit_list[-8]]

# 각 검증 비트들을 계산
c1 = str(reduce(lambda x, y: x ^ y, c1_bit))
c2 = str(reduce(lambda x, y: x ^ y, c2_bit))
c3 = str(reduce(lambda x, y: x ^ y, c3_bit))
c4 = str(reduce(lambda x, y: x ^ y, c4_bit))

#print(c4, c3, c2, c1)

# error_bit가 0인 경우(오류가 없는 경우)를 제외하고 해당 비트의 값 변경
error_bit = int(c4 + c3 + c2 + c1, 2)
if (error_bit == 0):
    pass

else:
    bit_list[-error_bit] = int(not bit_list[-error_bit])


# 실제 값이 아닌 체크 비트들을 리스트에서 제외
for i in not_real_value:
    del bit_list[i]

#print(bit_list)

# 각 index에 들어있는 비트의 값들을 합쳐 리스트로 변환
binary_num = ''.join(map(str, bit_list))
# 10진수로 출력
print(int(binary_num, 2))