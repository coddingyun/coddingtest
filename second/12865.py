n, k = map(int, input().split()) # 물품의 수, 최대 버틸 수 있는 무게

items = []
for i in range(n):
  items.append(list(map(int, input().split()))) # 무게, 가치

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
  for j in range(k+1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    elif items[i-1][0] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][k])

    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0;
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            #print(K[i][w], end=' ')
        #print('\n')
    return K[n][W]

