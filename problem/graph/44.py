import sys
input = sys.stdin.readline

def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x], parent)
  return parent[x]

def union_parent(x, y, parent):
  x = find_parent(x, parent)
  y = find_parent(y, parent)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

n = int(input())
parent = [0] * (n+1)

edges = []
total_cost = 0

x = []
y = []
z = []

for i in range(1, n+1):
  parent[i] = i
  data = list(map(int, input().split()))
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
  edges.append((x[i+1][0] - x[i][0], x[i+1][1], x[i][1]))
  edges.append((y[i+1][0] - y[i][0], y[i+1][1], y[i][1]))
  edges.append((z[i+1][0] - z[i][0], z[i+1][1], z[i][1]))

edges.sort()

for edge in edges:
  cost, x, y = edge
  if find_parent(x, parent) != find_parent(y, parent):
    union_parent(x, y, parent)
    total_cost += cost

print(total_cost)