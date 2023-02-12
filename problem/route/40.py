import heapq

n, m = map(int, input().split())
INF = int(1e9)

graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)
distance[1] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = []
for i in graph[1]:
  heapq.heappush(q, i)
  distance[i] = 1

while q:
  x = heapq.heappop(q)
  for i in graph[x]:
    if distance[i] > distance[x] + 1:
      distance[i] = min(distance[i], distance[x] + 1)
      heapq.heappush(q, i)

result = 0
for i in range(1, n+1):
  result = max(result, distance[i])

answer = []
for i in range(1, n+1):
  if result == distance[i]:
    answer.append(i)

print(answer[0], result, len(answer))