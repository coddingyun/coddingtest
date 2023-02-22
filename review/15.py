from collections import deque
import sys
input = sys.stdin.readline

n, m ,k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

q = deque([x])
visited[x] = True
dist = [int(1e9)] *(n+1)
dist[x] = 0

result = []
while q:
  nx = q.popleft()
  for i in graph[nx]:
    if visited[i] == False:
      q.append(i)
      visited[i] = True
      dist[i] = min(dist[nx] + 1, dist[i])
      
for i in range(len(dist)):
  if dist[i] == k:
    result.append(i)
if len(result) == 0:
  print(-1)
else:
  for data in result:
    print(data)