from collections import deque

n, k = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

q = deque()
visited = [[False]*k for _ in range(n)]

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      q.append([graph[i][j], i, j, 0])
      visited[i][j] = True

q = deque(sorted(q))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

while q:
  num, nx, ny, sec = q.popleft()
  if sec == s:
    break
  for i in range(4):
    tx = nx+dx[i]
    ty = ny+dy[i]
    if tx>=0 and tx<n and ty>=0 and ty<n and visited[tx][ty] == False:
      q.append([num, tx, ty, sec + 1])
      visited[tx][ty] = True
      graph[tx][ty] = num

print(graph[x-1][y-1])