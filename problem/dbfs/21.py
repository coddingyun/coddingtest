from collections import deque

n, mini, maxi = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0
def bfs(x, y, index):
  #r = False
  #visited = [[False]*n for _ in range(n)]
  #union = [[0]*n for _ in range(n)]
  united = []
  united.append((x, y))
  q = deque()
  q.append((x, y))
  union[x][y] = index
  summary = graph[x][y]
  count = 1
  while q:
    nx, ny = q.popleft()
    for i in range(4):
      tx = nx + dx[i]
      ty = ny + dy[i]
      if tx>=0 and tx<n and ty>=0 and ty<n and union[tx][ty] == -1:
        value = abs(graph[nx][ny] - graph[tx][ty])
        if value >= mini and value <= maxi:
          union[tx][ty] = index
          q.append((tx, ty))
          summary += graph[tx][ty]
          count += 1
          united.append((tx, ty))
  for i, j in united:
    graph[i][j] = summary//count
  return count

total_count = 0
while True:
  union = [[-1]*n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        bfs(i, j, index)
        index += 1
  if index == n*n:
    breakpoint
  total_count += 1

print(total_count)
