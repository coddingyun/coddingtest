import heapq

n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y,z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist +i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

total = 0
maximum = 0
for i in range(1, n+1):
  if distance[i] == INF:
    continue
  else:
    total+=1
    maximum = max(maximum, distance[i])

print(total-1, maximum)