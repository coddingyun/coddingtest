loads = list(map(int, input().split()))

s = sum(loads)

target = int(s // 2)


dp = [0]*(target+1)

for load in loads:
  for i in range(target, -1, -1): # 가장 큰 값 부터 넣어본다
    if i - load >=0 :
      dp[i] = max(dp[i], dp[i-load] + load)

print(s-dp[-1]*2)