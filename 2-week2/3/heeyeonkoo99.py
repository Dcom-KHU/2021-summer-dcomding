#2주차 3
#bfs/dfs문제이다.
#여행경로

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
        routes[r].sort(reverse=True)
    
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
   

    answer=" ".join(path[::-1])
    
    
    return answer

solution()

#Review)헷갈리면 https://gurumee92.tistory.com/165 사이트 다시한번 읽어보자