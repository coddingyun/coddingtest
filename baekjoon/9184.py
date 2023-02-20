

def w(a, b, c, dp):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  elif dp[a][b][c] != -1:
    return dp[a][b][c]
  elif a > 20 or b > 20 or c > 20:
    dp[a][b][c] = w(20, 20, 20, dp)
  elif a < b and b < c:
    dp[a][b][c] = w(a, b, c-1, dp) + w(a, b-1, c-1, dp) - w(a, b-1, c, dp)
  else:
    dp[a][b][c] = w(a-1, b, c, dp) + w(a-1, b-1, c, dp) + w(a-1, b, c-1, dp) - w(a-1, b-1, c-1, dp)
  return dp[a][b][c]


while True:
  array = list(map(int, input().split())) 
  if array == [-1, -1, -1]:
    break
  if array[0] <= 0 or array[1] <= 0 or array[2] <= 0:
    print(("w("+str(array[0]) +", "+str(array[1])+", "+str(array[2])+") = "+"1"))
    continue
  dp = [[[-1]*(array[2]+1) for _ in range(array[1]+1)] for _ in range(array[0]+1)]
  print("w("+str(array[0]) +", "+str(array[1])+", "+str(array[2])+") = "+ str(w(array[0], array[1], array[2], dp)))