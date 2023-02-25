# 효율적인 화폐 구성: k를 만드는 최소의 코인 개수
k = 100
dp = [int(1e9)] * (k+1)

for coin in coins:
  for i in range(coin, k+1):
    dp[i] = min(dp[i], dp[i-coin]+1)


# 동전 1: 특정 금액을 만들 수 있는 조합의 수

for coin in coins:
  for i in range(coin, k+1):
    dp[i] += dp[i-coin]