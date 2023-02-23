n = int(input())

graph = []
dp = [0]*(n+1)

for i in range(n):
  graph.append(list(map(int, input().split())))

for i in range(n):
  t = i+graph[i][0]
  if t <= n:
    for j in range(t, n+1):
      dp[j] = max(dp[j], dp[i]+graph[i][1])

print(max(dp))