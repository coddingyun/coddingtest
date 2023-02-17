n = int(input())

stairs = []
for i in range(n):
  stairs.append(int(input()))

dp = [[[0,0],[0,0]] for _ in range(n+1)]
dp[1][0][0] = stairs[0]
dp[1][0][1] = 1
if n>1:
  dp[2][1][0] = stairs[1]
  dp[2][1][1] = 1
  
for i in range(1, n+1):
  for j in range(2):
    if dp[i][j][1] == 2:
      if i+2 < n+1 and dp[i+2][j][0] < dp[i][j][0]+stairs[i+1]:
        dp[i+2][j][0] = dp[i][j][0]+stairs[i+1]
        dp[i+2][j][1] = 1
    if dp[i][j][1] == 1:
      if i+1 < n+1 and dp[i+1][j][0] < dp[i][j][0]+stairs[i]:
        dp[i+1][j][0] = dp[i][j][0]+stairs[i]
        dp[i+1][j][1] = 2
      if i+2 < n+1 and dp[i+2][j][0] < dp[i][j][0]+stairs[i+1]:
        dp[i+2][j][0] = dp[i][j][0]+stairs[i+1]
        dp[i+2][j][1] = 1

print(max(dp[n][0][0], dp[n][1][0]))


n = int(input())

data = [0]

for i in range(n):
    data.append(int(input()))

dp = [0] * (n+1)
dp[1] = data[1]

for i in range(2,n+1):
    dp[i] = max(data[i]+dp[i-2],data[i]+data[i-1] + dp[i-3])

print(dp[n])