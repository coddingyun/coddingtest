from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

zero = []
bees = []

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      zero.append([i, j])
    elif graph[i][j] == 2:
      bees.append([i, j])

coms = list(combinations(zero, 3))

q = deque()
for bee in bees:
  q.append(bee)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0

def number_zero(graph):
  total = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        total += 1
  return total

for com in coms:
  graph2 = copy.deepcopy(graph)
  for i in com:
    x, y = i
    graph2[x][y] = 1
  qcopy = deque()
  qcopy = copy.deepcopy(q)
  while qcopy:
    nx, ny = qcopy.popleft()
    for j in range(4):
      px = nx + dx[j]
      py = ny + dy[j]
      #print(px, py)
      if px>=0 and px<n and py>=0 and py<m and graph2[px][py] == 0:
        #print(px, py)
        qcopy.append([px, py])
        graph2[px][py] = 2
  result = max(result, number_zero(graph2))
  #print(graph2)

print(result)
        
  
