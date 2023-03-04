# dfs/bfs 가 안되는 이유: 좌표를 옮길때마다 비용이 다 다르기 때문에
import heapq

for _ in range(int(input())):
  graph = []
  n = int(input())
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  INF = int(1e9)
  distance = [[INF]*n for _ in range(n)]

  q = []
  heapq.heappush(q, (graph[0][0], 0, 0))
  distance[0][0] = graph[0][0]
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=0 and ny>=0 and nx<n and ny<n:
        cost = graph[nx][ny] + dist # graph 만 조심
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))

  print(distance[n-1][n-1])
    