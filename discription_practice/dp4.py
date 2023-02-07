n,m = map(int, input().split())

array = []

for i in range(n):
  array.append(int(input()))

array.sort()

dp = [10000] * 10001

for i in array:
  dp[i]=1

for i in range(1,m+1):
  for j in range(n):
    point = array[j]
    if dp[i-point] != 10000:
      dp[i] = min(dp[i], dp[i-point]+1)

if dp[m] == 10000:
  print(-1)
else:
  print(dp[m])
  