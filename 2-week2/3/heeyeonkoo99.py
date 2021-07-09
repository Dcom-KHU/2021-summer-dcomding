#2주차 3
#bfs/dfs문제이다.
#여행경로


def order_by_alphabet(array):
    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]<=array[j]:
                array[i],array[j]=array[j],array[i]

def solution():
    routes=dict()
    answer=""

#그래프 생성
    for i in range(int(input())):
        start,end=map(str,input().split())
        if start==end:
            continue
        else:
            routes[start]=routes.get(start,[])+[end]

    for r in routes.keys():
        #우선 'len'=>'알파벳 순서'로 중요도를 줘야 한다.
        routes[r].sort(key=len,reverse=True)
        order_by_alphabet(routes[r])

    #print(routes)
   
    stack=["DCOM"]
    path=[]
    #print(routes)- 체크용
    
    while stack:
        top=stack[-1]
    
        if top not in routes or len(routes[top])==0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top]=routes[top][:-1]
   

    for i in path[::-1]:
        print(i,end=" ")

solution()

#Review)헷갈리면 https://gurumee92.tistory.com/165 사이트 다시한번 읽어보자