n = int(input())
array = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
  cnt = 0
  for j in range(i):
    if array[j] < array[i] and cnt < dp[j]:
      cnt = dp[j]
  dp[i] += cnt

print(max(dp))