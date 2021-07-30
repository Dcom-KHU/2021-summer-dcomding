# 어딜 폐업할지는 결국 다 해봐야 알 수 있을 듯.
# 근데 그걸 다 해볼 때 마다 치킨 거리를 매번 구하는 것 보다는
# 각 치킨가게에 대한 거리를 모두 구해놓고 매번 그 값들 중 최솟값을 치킨거리로 하는 게 좋을 듯?

from itertools import combinations

N, M = map(int, input().split())
coords = []
chickens = []
houses = []

for r in range(N):
    coords.append([])
    for c, val in enumerate(map(int, input().split())):
        if val == 2:
            chickens.append((r, c))
        elif val == 1:
            houses.append((r,c))
        coords[-1].append(val)

# 각 집들의 치킨집과의 거리들을 기록
chicken_distances = [[101] * len(chickens) for _ in range(len(houses))]
for house_idx, house in enumerate(houses):
    for chicken_idx, chicken in enumerate(chickens):
        chicken_distances[house_idx][chicken_idx] = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

answers = []
for chicken_comb in combinations(range(len(chickens)), M):
    sum_of_valid_chicken_dists = 0
    for cd_for_house in chicken_distances:
        min_tmp = 101
        for chicken_idx, dist in enumerate(cd_for_house):
            if chicken_idx in chicken_comb:
                min_tmp = min(min_tmp, dist)
        sum_of_valid_chicken_dists += min_tmp
    answers.append(sum_of_valid_chicken_dists)
print(min(answers))
