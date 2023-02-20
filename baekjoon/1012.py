dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, b, visited, graph):
  global n, m
  visited[a][b] = True
  for i in range(4):
    tx = a+dx[i]
    ty = b+dy[i]
    if tx>=0 and ty>=0 and tx<m and ty<n and visited[tx][ty] == False and graph[tx][ty] == 1:
      bfs(tx, ty, visited, graph)

for _ in range(int(input())):
  m, n, k = map(int, input().split())
  graph = [[0]*n for _ in range(m)]
  visited = [[False]*n for _ in range(m)]
  for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
  total = 0
  for i in range(m):
    for j in range(n):
      if visited[i][j] == False and graph[i][j] == 1:
        bfs(i, j, visited, graph)
        total +=1
  print(total)

