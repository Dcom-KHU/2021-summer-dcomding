# 해밍코드...

def xor(*nums):
    r = nums[0]
    for n in nums[1:]:
        r = r ^ n
    return r

def get_parity_bits(nums):
    return [nums[-8], nums[-4], nums[-2], nums[-1]]

numbers = list(map(int, input().split()))
numbers.reverse()
parities = get_parity_bits(numbers)
c1 = xor(numbers[2], numbers[4], numbers[6], numbers[8], numbers[10], numbers[12], numbers[14], numbers[0])
c2 = xor(numbers[2], numbers[5], numbers[6], numbers[9], numbers[10], numbers[13], numbers[14], numbers[1])
c3 = xor(numbers[4], numbers[5], numbers[6], numbers[11], numbers[12], numbers[13], numbers[14], numbers[3])
c4 = xor(numbers[8], numbers[9], numbers[10], numbers[11], numbers[12], numbers[13], numbers[14], numbers[7])

error_bit = c4 * (2**3) + c3 * (2**2) + c2 * (2) + c1
numbers[-error_bit] = numbers[-error_bit] ^ 1
bin_nums = numbers[2:3] + numbers[4:7] + numbers[8:15]
bin_num = int('0b'+''.join(map(str, bin_nums)), 2)
print(bin_num)