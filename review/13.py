from itertools import combinations

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chickens.append([i, j])
    if graph[i][j] == 1:
      houses.append([i, j])

candidates = list(combinations(chickens, m))
subgraph = [[0]*n for _ in range(n)]
min_chicken_distance = int(1e9)

for candidate in candidates:
  chicken_distance = 0
  for house in (houses):
    hx, hy = house
    answer = int(1e9)
    for i in range(len(candidate)):
      x, y = candidate[i]
      answer = min(answer, abs(x-hx) + abs(y-hy))
    chicken_distance += answer
  min_chicken_distance = min(min_chicken_distance, chicken_distance)

print(min_chicken_distance)
  