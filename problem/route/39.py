import heapq

t = int(input())

for _ in range(t):
  n = int(input())

  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  dx = [0,0,1,-1]
  dy = [1,-1,0,0]

  INF = int(1e9)
  dp = [[INF]*n for _ in range(n)]
  dp[0][0] = graph[0][0]
  q = []
  heapq.heappush(q, (graph[0][0], 0,0))

  while q:
    dist, x, y = heapq.heappop(q)
    if dist > dp[x][y]:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <0 or nx >=n or ny<0 or ny>=n:
        continue
      else:
        if dp[nx][ny] > dp[x][y] + graph[nx][ny]:
          heapq.heappush(q, (graph[nx][ny], nx, ny))
          dp[nx][ny] = dp[x][y] + graph[nx][ny]

  print(dp[n-1][n-1])