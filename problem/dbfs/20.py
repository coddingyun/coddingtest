from itertools import combinations
import copy
from collections import deque

n = int(input())

graph = []

for i in range(n):
  graph.append(list(input().split()))

candidates = []
teachers = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'X':
      candidates.append((i, j))
    if graph[i][j] == 'T':
      teachers.append((i, j))

datas = list(combinations(candidates, 3))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 'NO'

for data in datas:
  r = True
  graph2 = copy.deepcopy(graph)
  q = deque(teachers)
  for i in data:
    x = i[0]
    y = i[1]
    graph2[x][y] = 'O'
  while q:
    nx, ny = q.popleft()
    for j in range(4):
      tx, ty = nx, ny
      while tx+dx[j]>=0 and tx+dx[j]<n and ty+dy[j]>=0 and ty+dy[j]<n:
        tx += dx[j]
        ty += dy[j]
        if graph2[tx][ty] == 'S':
          r = False
          break
        if graph2[tx][ty] == 'O':
          break
  if r == True:
    answer = 'YES'
    break

print(answer)
      
  