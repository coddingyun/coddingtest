n = int(input())

dp = [0] * 30001

dp[1]=0
dp[2]=1

def func(a):
  for i in range(3,a+1):
    first = 100000
    second = 100000
    third = 100000
    if i%5==0:
      first = 1+dp[i//5]
    if i%3 == 0:
      second = 1+dp[i//3]
    if i%2 == 0:
      third= 1+dp[i//2]
    fourth=1+dp[i-1]
    dp[i] = min(first, second, third, fourth)
  
func(n)
print(dp[n])
'''
def funct(a):
  print(a)
  if dp[a]>0:
    return dp[a]

  if a%5==0:
    return 1+func(a//5)
  elif a%3==0:
    return 1+func(a//3)
  elif a%2 ==0:
    return 1+func(a//2)
  else:
    return 1+func(a-1)
'''

