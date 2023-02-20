import sys
input = sys.stdin.readline
n = int(input())
'''시간초과
total = 0
def result(number, cnt):
  global total
  if cnt == n:
    total += 1
    return 
  if number-1>=0:
    result(number-1, cnt+1)
  if number+1<=9:
    result(number+1, cnt+1)

for i in range(1, 10):
  result(i, 1)

print(total)
'''
dp =[[0]*10 for _ in range(n+1)]

for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  dp[i][0] = dp[i-1][1]
  for j in range(1,9):
    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000
  dp[i][9] = dp[i-1][8]

print(sum(dp[n])%1000000000)