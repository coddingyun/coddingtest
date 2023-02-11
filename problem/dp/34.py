n = int(input())

array = list(map(int, input().split()))

dp = [1] * (n)

for i in range(1, n):
  j = i
  maxi = 0
  while j-1>=0:
    if array[j-1]> array[i]: 
      maxi = max(maxi, dp[j-1])
    j-=1
  dp[i] = maxi + 1

print(n-max(dp))