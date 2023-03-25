from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

totalo = 0
graph = []
for i in range(n):
  li = list(input())
  graph.append(li)
  totalo += li.count('O')

a, b = map(int, input().split())
graph2 = []
for i in range(a):
  graph2.append(list(input()))

#print(graph2)

max_x = max(n,a)
max_y = max(m,b)

expand_graph = [["_"]*max_y*3 for _ in range(max_x*3)]
expand_graph2 = [["_"]*max_y*3 for _ in range(max_x*3)]

#[[-1]*2 for _ in range(100001)]


for i in range(n):
  for j in range(m):
    k = graph[i][j]
    expand_graph[i][j] = k

for i in range(a):
  for j in range(b):
    expand_graph2[i+max_x][j+max_y] = graph2[i][j]

#print(expand_graph)
#print(expand_graph2)

visited = [[False]*max_y*2 for _ in range(max_x*2)]


def check(graph1, graph2, x, y):
  result = 0
  for i in range(max_x):
    for j in range(max_y):
      if graph1[i][j] == graph2[i+x][j+y] and graph1[i][j] == 'O':
        result += 1
  return result

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()

q.append((0,0))
visited[0][0] = True

result = 0

while q:
  nx, ny = q.popleft()

  result = max(result, check(expand_graph, expand_graph2, nx, ny))
  
  for i in range(4):
    tx = nx + dx[i]
    ty = ny + dy[i]
    if tx>=0 and tx<max_x*2 and ty>=0 and ty<max_y*2 and visited[tx][ty] == False:
      q.append((tx, ty))
      visited[tx][ty] = True

print(totalo- result)
      