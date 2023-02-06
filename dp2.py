n = int(input())

array = list(map(int, input().split()))
dp = [0]*1001

dp[1] = array[0]
dp[2] = max(array[1],array[0])

for i in range(2,n+1):
  dp[i] = max(dp[i-1], array[i-1]+dp[i-2])
  

print(dp[n])