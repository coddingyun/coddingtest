from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

INF = int(1e9)
distance = [INF] * (n+1)
distance[x] = 0

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

q=deque()
q.append(x)
visited[x] = True

while q:
  now = q.popleft()
  for i in graph[now]:
    if visited[i] == False:
      distance[i] = min(distance[i], distance[now] + 1)
      q.append(i)
      visited[i] = True

total = 0
for i in range(n+1):
  if distance[i] == k:
    total += 1
    print(i)

if total == 0:
  print(-1)
    