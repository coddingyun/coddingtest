k = int(input())


for _ in range(k):
  n = int(input())
  INF = int(1e9)
  dp = [0] * (n+3)
  
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4
  for i in range(4, n+1):
    dp[i] += dp[i-1]
    dp[i] += dp[i-2]
    dp[i] += dp[i-3]
  
  print(dp[n])