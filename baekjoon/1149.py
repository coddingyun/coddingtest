n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF]*n for _ in range(n)]

dp[0] = graph[0]

for i in range(1, n):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + graph[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + graph[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + graph[i][2]

print(min(dp[n-1]))