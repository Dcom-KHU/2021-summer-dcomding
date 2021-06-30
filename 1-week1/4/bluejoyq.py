import math
def solve():
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    if N == 1:
        print(values[0])
    else:
        # -1 idx가 나올 경우 항상 선택하지 않기 위해
        values.append(-1) 
        tree_length = pow(2,math.ceil(math.log(N,2))+1)-1
        tree_list = [0]*(tree_length)

        def init(node, start, end):
            if start == end :
                tree_list[node] = start
                return tree_list[node]
            else :
                left_idx = init(node*2, start, (start+end)//2)
                right_idx = init(node*2+1, (start+end)//2+1, end)
                if values[left_idx] > values[right_idx]:
                    tree_list[node] = left_idx
                else:
                    tree_list[node] = right_idx
                return tree_list[node]

        def get_max(idx,left,right,start, end):
            if left > end  or right < start:
                return -1
            if left <= start and end <= right:
                return tree_list[idx]

            mid = (start + end) // 2
            left_idx = get_max(idx * 2, left, right, start, mid)
            right_idx = get_max(idx*2 + 1,left,right, mid+1, end)
            if values[left_idx] > values[right_idx]:
                return left_idx
            else:
                return right_idx



        init(1,0,N-1)
        result = 12312312412
        tmp = -1
        for i in range(N - K + 1):
            if tmp >= i:
                if values[i] < values[tmp]:
                    continue
                tmp = i
            else:
                left = i 
                right = i + K - 1
                tmp = get_max(1, left, right, 0, N - 1)
            result = min(result, values[tmp])
        print(result)
solve()