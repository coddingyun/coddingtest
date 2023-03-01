import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

graph = []

for _ in range(r):
  graph.append(list(map(int, input().split())))

#print(sum(map(sum,graph))+2)

dx = [0,-1,0,1] # 동 북 서 남
dy = [1,0,-1,0]

while t>0:
  info = []
  for i in range(r):
    for j in range(c):
      if graph[i][j] != 0 and graph[i][j] != -1:
        info.append([i, j, graph[i][j]])
  for data in info:
    x, y, amount = data
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx>=0 and nx<r and ny>=0 and ny<c and graph[nx][ny] != -1:
        graph[nx][ny] += amount//5
        graph[x][y] -= amount//5

  for i in range(r):
    if graph[i][0] == -1:
      dir = 0
      x = i
      y = 0
      nx = x+dx[dir]
      ny = y+dy[dir]
      pre = 0
      while nx!=i or ny!=0:
        graph[nx][ny], pre = pre, graph[nx][ny]
        nx = nx + dx[dir]
        ny = ny + dy[dir]
        if nx<0 or ny>=c or ny<0:
          nx -= dx[dir]
          ny -= dy[dir]
          dir = (dir+1)%4
          nx += dx[dir]
          ny += dy[dir]
      dir = 0
      x = i+1
      y = 0
      nx = x+dx[dir]
      ny = y+dy[dir]
      pre = 0
      while nx!=i+1 or ny!=0:
        #print(nx, ny)
        graph[nx][ny], pre = pre, graph[nx][ny]
        nx = nx + dx[dir]
        ny = ny + dy[dir]
        if ny>=c or ny<0 or nx>=r:
          nx -= dx[dir]
          ny -= dy[dir]
          dir = (dir-1)%4
          nx += dx[dir]
          ny += dy[dir]   
      break
  t -= 1
#for i in range(c):
#  print(graph[i])

print(sum(map(sum,graph))+2)