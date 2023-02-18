n = int(input())

graph =[]
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

cnt = 0
def dfs(a, b):
  graph[a][b] = 0
  global cnt 
  cnt += 1
  for i in range(4):
    tx = a+dx[i]
    ty = b+dy[i]
    if tx>=0 and tx<n and ty>=0 and ty<n and graph[tx][ty] == 1:
      dfs(tx, ty)  


result = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt = 0
      dfs(i, j)
      result.append(cnt)

result.sort()
print(len(result))
for i in result:
  print(i)