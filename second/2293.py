n, k = map(int, input().split())

coins = []
dp =[0]*(k+1)

for _ in range(n):
  coin = int(input())
  coins.append(coin)
  #dp[coin] = 1

dp[0] = 1


for coin in coins:
  for i in range(coin, k+1):
    dp[i] += dp[i-coin]

for i in range(1, k+1):
  for coin in coins:
    if i-coin>= 0:
      dp[i] += dp[i-coin]

'''
for j in coins:
  for i in range(j, k+1):
      dp[i] += dp[i-j]
1 += 0
2 += 1
3 += 2
2+= 0
3+= 1
5 +=3
'''

print(dp[k])

