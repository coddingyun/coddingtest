import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

INF = int(1e9)
distance = [INF]*(n+1)

q = []
heapq.heappush(q, (0, 1)) #거리, 출발 헛간 번호
distance[1] = 0


while q:
  dist, now = heapq.heappop(q)
  if dist > distance[now]:
    continue
  for i in graph[now]:
    cost = distance[now] + 1
    if cost < distance[i]:
      distance[i] = cost
      heapq.heappush(q, (cost, i))

length = 0
for i in range(1, n+1):
  if distance[i] != INF:
    if length < distance[i]:
      length = distance[i]

for i in range(1, n+1):
  if distance[i] == length:
    print(i, length, end=' ')
    print(distance.count(length))
    break