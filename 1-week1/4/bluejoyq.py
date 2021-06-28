import math

N, K = map(int, input().split())
values = list(map(int, input().split()))
if N == 1:
    print(values[0])
else:
    tree_length = pow(2,math.ceil(math.log(N,2))+1)-1
    tree_list = [0]*(tree_length)
    
    def init(node, start, end):
        if start == end :
            tree_list[node] = values[start]
            return tree_list[node]
        else :
            tree_list[node] = max(init(node*2, start, (start+end)//2) , init(node*2+1, (start+end)//2+1, end))
            return tree_list[node]
    
    def get_max(idx,left,right,start, end):
        if left > end  or right < start:
            return -1
        if left <= start and end <= right:
            return tree_list[idx]
        
        mid = (start + end) // 2
        return max(get_max(idx * 2, left, right, start, mid), get_max(idx*2 + 1,left,right, mid+1, end))
    
    
    init(1,0,N-1)
    result = 12312312412
    for i in range(N - K):
        left = i 
        right = i + K 
        tmp = get_max(1, left, right, 0, N)
        result = min(result, tmp)
    print(result)
    #[2 ,4 ,5 ,3 ,2 ,1 ,4 ,2 ,5, 1]