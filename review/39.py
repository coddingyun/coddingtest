from collections import deque
import heapq

for _ in range(int(input())):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  INF = int(1e9)
  distance = [[INF]*n for _ in range(n)]

  q = []
  heapq.heappush(q, (graph[0][0], 0, 0)) #거리, x값, y값
  distance[0][0] = graph[0][0]

  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  while q:
    dist, nx, ny = heapq.heappop(q)
    if dist > distance[nx][ny]:
      continue
    for i in range(4):
      tx = nx + dx[i]
      ty = ny + dy[i]
      if tx>=0 and tx<n and ty>=0 and ty<n:
        cost = distance[nx][ny] + graph[tx][ty]
        if cost < distance[tx][ty]:
          distance[tx][ty] = cost
          heapq.heappush(q, (cost, tx, ty))

  print(distance[n-1][n-1])
        