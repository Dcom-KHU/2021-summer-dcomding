def solve():
    bits = list(map(int,input().split()))
    paritys = {
        1: [3, 5, 7, 9, 11, 13, 15,1],
        2: [3, 6, 7, 10, 11, 14, 15,2], 
        4: [5, 6, 7, 12, 13, 14, 15,4],
        8: [9, 10, 11, 12, 13, 14, 15,8]
    }
    datas = [3,5,6,7,9,10,11,12,13,14,15]
    error_idx = ""
    bits.insert(0,0)
    for p in paritys.values():
        tmp = bits[p[0]]
        for idx in p[1:]:
            tmp ^= bits[idx]
        error_idx += str(tmp)
    target_idx =int(error_idx[::-1],2)
    
    bits[target_idx] = int(not bits[target_idx])
    result = ""
    for data in datas[::-1]:
        result += str(bits[data])
    print(int(result,2))
solve()