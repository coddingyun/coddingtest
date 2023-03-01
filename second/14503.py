import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

robots = list(map(int, input().split()))

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

  
#$0$인 경우 북쪽, $1$인 경우 동쪽, $2$인 경우 남쪽, $3$인 경우 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

def clean(x, y, dir):
  global answer
  if graph[x][y] == 0:
    graph[x][y] = 2
    answer += 1
    #print(answer)
  r = False
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny] == 0:
      r = True
  if r == True:
    while True:
      dir = (dir+3)%4
      tx = x+dx[dir]
      ty = y+dy[dir]
      if tx>=0 and ty>=0 and tx<n and ty<m and graph[tx][ty] == 0:
        return clean(tx, ty, dir)
  else:
    tx = x-dx[dir]
    ty = y-dy[dir]
    if tx>=0 and ty>=0 and tx<n and ty<m and graph[x-dx[dir]][y-dy[dir]] != 1:
      return clean(x-dx[dir], y-dy[dir], dir)
    else:
      return answer

print(clean(robots[0], robots[1], robots[2]))
    