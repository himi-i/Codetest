
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

answer = float('inf')


for comb in combinations(chickens, M):
    total = 0

    for hx, hy in houses:
        dist = float('inf')

        for cx, cy in comb:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))

        total += dist

    answer = min(answer, total)

print(answer)
