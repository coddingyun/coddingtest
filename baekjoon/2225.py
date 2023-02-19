n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(0, n+1):
  dp[i][1] = 1


for i in range(0, n+1):
  for j in range(0, i+1):
    for p in range(2, k+1):
      dp[i][p] += dp[j][p-1]

print(dp[n][k]%1000000000)
