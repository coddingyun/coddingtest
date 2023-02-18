n, k = map(int, input().split())

coins = []
dp = [0]*(k+1)
for i in range(n):
  coin = int(input())
  coins.append(coin)

dp[0] = 1


for j in coins:
  for i in range(j, k+1):
    if i-j>=0 :
      dp[i] += dp[i-j]
  
print(dp[k])
