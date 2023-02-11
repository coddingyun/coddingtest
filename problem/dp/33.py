n = int(input())

array = []
dp = [0] * (n+1)

for i in range(n):
  array.append(list(map(int, input().split())))

for i in range(n):
  if i+array[i][0] < n+1:
    value = dp[i + array[i][0]] 
    value = max(value, dp[i] + array[i][1])
    for j in range(i + array[i][0], n+1):
      dp[j] = max(value, dp[j])


print(max(dp))
