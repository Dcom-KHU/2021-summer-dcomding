n, k = map(int, input().split())
moves = list(map(int, input().split()))
basket = list()
result = 0
'''
zip
1) input: 여러 개의 iterable 객체들
2) output: 각 iterable 객체의 iterator들을 순차적으로 tuple 형태로 return
           iter 횟수는 인자로 받은 iterable 객체 중 최소 길이와 같음
           
*argument
: iterable unpacking(argument == iterable object)
=> 인자의 개수가 가변할 때 사용하는 것이 좋을 듯

Thank you for SolidCitadel...
'''

board = [list(filter(lambda x : x != 0, reversed(r))) for r in zip(*[map(int, input().split()) for i in range(n)])]

for m in moves:
    if not board[m-1]:
        continue
        
    d = board[m-1].pop()
    
    if basket and d == basket[-1]:
        basket.pop()
        result += 2
            
    else:
        basket.append(d)
        
print(result)