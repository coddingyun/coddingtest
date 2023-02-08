from collections import deque
import copy
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

s, tx, ty = map(int, input().split())

data = []

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0 :
      data.append((graph[i][j], 0, i, j))

data.sort() # deque는 sort가 안되기 때문에 list로 sort한 후 queue에 넣어준다
q = deque(data)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

while q:
  num, sec, x, y = q.popleft()
  if sec == s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and ny>=0 and nx<n and ny<n and graph[nx][ny] == 0:
      graph[nx][ny] = num
      q.append((graph[nx][ny], sec+1, nx, ny))

print(graph[tx-1][ty-1])
    