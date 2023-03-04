import sys
input = sys.stdin.readline

n = int(input())

x = []
y = []
z = []

for t in range(n):
  i, j, k = map(int, input().split())
  x.append((i, t))
  y.append((j, t))
  z.append((k, t))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n-1):
  edges.append([x[i+1][0]-x[i][0], x[i][1], x[i+1][1]])
  edges.append([y[i+1][0]-y[i][0], y[i][1], y[i+1][1]])
  edges.append([z[i+1][0]-z[i][0], z[i][1], z[i+1][1]])

def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x], parent)
  return parent[x]

def union_parent(x, y, parent):
  x = parent[x]
  y = parent[y]
  if x>y:
    parent[x] = y
  else:
    parent[y] = x

parent = [i for i in range(n)]

edges.sort()
answer = 0

for edge in edges:
  dist, x, y = edge
  if find_parent(x, parent) != find_parent(y, parent):
    union_parent(x, y, parent)
    answer += dist

print(answer)
