def hamming(check_num, arr):
    check_digits = [
        [1, 3, 5, 7, 9, 11, 13, 15],
        [2, 3, 6, 7, 10, 11, 14, 15],
        [4, 5, 6, 7, 12, 13, 14, 15],
        [8, 9, 10, 11, 12, 13, 14, 15]
    ]
    result = 0
    for d in check_digits[check_num - 1]:
        result += arr[d - 1]

    return result % 2

def sum_arr(arr):
    check_digits = [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
    result = 0
    for i, d in enumerate(check_digits):
        result += arr[d - 1] * (2 ** i)
    return result

arr = list(map(int, input().split()))
bit_arr = [2 ** (i - 1) if hamming(i, arr) == 1 else 0  for i in range(1, 5)]
error_bit = sum(bit_arr)

if error_bit != 0:
    arr[error_bit - 1] = (arr[error_bit - 1] + 1) % 2

print(sum_arr(arr))
