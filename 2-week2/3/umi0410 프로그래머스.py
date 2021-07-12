# 끝까지 가는 경우 하나를 구하는 거면 DFS가 좋고
# 최단거리를 구해야하는 경우는 BFS가 좋다
# 이동할 때마다의 어떠한 aging 조건이 있으면 DFS가 그 이동의 상태를 관리하기 편하다.
# 근데 이번 꺼는 끝까지 가는 모든 경우긴 해서 별 상관없을 것 같은데 DFS로 해봄.

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    N = len(tickets) # ticket이 2장이면 footprint는 3개가 되어야 끝남
    for depart, dest in tickets:
        graph[depart].append(dest)
    for key in graph:
        graph[key].sort()
    return dfs(N, 'ICN', graph, ['ICN'])



def dfs(N, depart, graph, footprint) ->list:
    # print(footprint)
    if len(footprint) == N + 1:
        return footprint
    for i, dest in enumerate(graph[depart]):
        # 이번 도착지는 빼고 dfs 한 번 호출 후
        # 완료하면 다시 추가함.
        graph[depart].pop(i)
        tmp_footprint = footprint[:]
        tmp_footprint.append(dest)
        ret = dfs(N, dest, graph, tmp_footprint)
        graph[depart].insert(i, dest)
        # 만약 끝까지 방문한 경우가 있다면 stack을 탈출하면서 걔를 리턴
        # 원래는 리턴값들을 다 구해서 sort한 애를 구했었는데
        # 애초에 sort 시켜서 리턴은 하나만 구하면 됨.
        if ret:
            return ret

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
