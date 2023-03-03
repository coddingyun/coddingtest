from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [[-1]*2 for _ in range(100001)]
visited[n][0] = 0
visited[n][1] = 1

while q:
  now = q.popleft()
  for i in [now-1, now+1, now*2]:
    if 0<= i <= 100000:
      if visited[i][0] == -1: # 처음이라면
        visited[i][0] = visited[now][0] + 1
        visited[i][1] = visited[now][1]
        q.append(i)
      elif visited[i][0] == visited[now][0] + 1:
        visited[i][1] += visited[now][1]

print(visited[k][0])
print(visited[k][1])

  
