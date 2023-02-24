def find_parent(parent, x):
  if x != parent[x]:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

n = int(input())

parent = [i for i in range(n)]
x = []
y = []
z = []

for i in range(n):
  a, b, c= map(int, input().split())
  x.append((a, i))
  y.append((b, i))
  z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
  edges.append((abs(x[i+1][0] - x[i][0]), x[i][1], x[i+1][1]))
  edges.append((abs(y[i+1][0] - y[i][0]), y[i][1], y[i+1][1]))
  edges.append((abs(z[i+1][0] - z[i][0]), z[i][1], z[i+1][1]))

edges.sort()
result = 0

for edge in edges:
  dist, nx, ny = edge
  if find_parent(parent, nx) != find_parent(parent, ny):
    union_parent(parent, nx, ny)
    result += dist

print(result)
