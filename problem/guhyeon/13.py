from itertools import combinations

n, m = map(int, input().split())

array = []

for i in range(n):
  array.append(list(map(int, input().split())))

distance = []
houses = []
chickens = []

for i in range(n):
  for j in range(n):
    if array[i][j] == 1:
      houses.append((i,j))
    elif array[i][j] == 2:
      chickens.append((i,j))

candidates = list(combinations(chickens,m))

def sum_dis(chickens, houses):
  min_distance = []
  for house in houses:
    realdis = int(1e9)
    hx, hy = house
    for i in range(m):
      x, y = chickens[i]
      realdis = min(realdis, abs(x-hx)+abs(y-hy))
    min_distance.append(realdis)
  return sum(min_distance)

for candidate in candidates:
  distance.append(sum_dis(candidate, houses))

distance.sort()
print(distance[0])
    

