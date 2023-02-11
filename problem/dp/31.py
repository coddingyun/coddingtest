t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  INF = int(1e9)
  dp = [[0]*m for _ in range(n)]
  array = list(map(int, input().split()))
  for j in range(n):
    for k in range(m):
      graph[j][k] = array[0]
      array.pop(0)
  for j in range(m):
    dp[0][j] = graph[0][j]
  for j in range(n):
    dp[j][0] = graph[j][0]
  for k in range(1, m):
    for j in range(1, n):
      #print(j, k)
      if j + 1 < n:
        dp[j][k] = max(dp[j-1][k-1], dp[j][k-1], dp[j+1][k-1]) + graph[j][k]
      else:
        dp[j][k] += max(dp[j-1][k-1], dp[j][k-1]) + graph[j][k]
      #print(dp)
        
  #print(dp)
  print(max(map(max, dp)))

  