n, l, r = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(a, b):
  global dx, dy, n, united, visited, l, r
  if visited[a][b] == False:
    visited[a][b] = True
    united.append((a,b, graph[a][b]))
    for i in range(4):
      tx = a + dx[i]
      ty = b + dy[i]
      #print(tx, ty, l, r)
      if tx>=0 and tx<n and ty>=0 and ty<n and visited[tx][ty] == False and l <= abs(graph[tx][ty]-graph[a][b]) <= r:
        #print("hi")
        dfs(tx, ty)

result = 0
while True:
  visited = [[False]*n for _ in range(n)]
  check = False
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        united = []
        dfs(i, j)
        #print(united)
        if len(united) > 1:
          total = 0
          check = True
          for data in united:
            total += data[2]
          val = int(total//len(united))
          for data in united:
            graph[data[0]][data[1]] = val
  if check == False:
    break
  result += 1

print(result)