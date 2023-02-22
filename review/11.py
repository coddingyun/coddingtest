from collections import deque

n = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

k = int(input())

for _ in range(k):
  a, b = map(int, input().split())
  graph[a][b] = 1

t = int(input())

directions = []
for _ in range(t):
  directions.append(list(input().split()))

def check(x, y, graph):
  if x<=0 or y<=0 or x>n or y>n or graph[x][y] == 2:
    return False
  return True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bam(graph, directions):
  q = deque()
  q.append((1, 1))
  idx = 0
  pre = 0
  x = y = 1
  graph[x][y] = 2
  cnt = 0
  while True:
    for i in range(t):
      tval = int(directions[i][0])-pre
      if tval < 0:
        break
      for j in range(tval):
        x = x + dx[idx]
        y = y + dy[idx]
        q.append((x,y))

        if x>0 and y>0 and x<=n and y<=n and graph[x][y] == 0:
          lx, ly = q.popleft()
          graph[lx][ly] = 0
        if check(x, y, graph) == False:
          return pre+j+1
        graph[x][y] = 2
      pre = int(directions[i][0])
      if directions[i][1] == 'L':
        idx = idx-1
        if idx == -1:
          idx = 3
      else:
        idx = idx + 1
        if idx == 4:
          idx = 0
    x = x + dx[idx]
    y = y + dy[idx]
    q.append((x,y))

    if x>0 and y>0 and x<=n and y<=n and graph[x][y] == 0:
      lx, ly = q.popleft()
      graph[lx][ly] = 0
    if check(x, y, graph) == False:
      return pre+cnt+1
    graph[x][y] = 2
    cnt += 1

print(bam(graph, directions))