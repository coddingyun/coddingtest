n, m = map(int, input().split())

parent = [0]*(n+1)

def find_parent(a):
  if parent[a]!=a:
    parent[a]=find_parent(parent[a])
  return parent[a]

def union_set(a,b):
  x = find_parent(a)
  y = find_parent(b)
  if x>y:
    parent[a]=y
  else:
    parent[b]=x

edges = []

for i in range(1, n+1):
  parent[i]=i

for i in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

max_cost = 0
total_cost = 0

for edge in edges:
  if find_parent(edge[1]) == find_parent[edge[2]]:
    continue
  else:
    union_set(edge[1], edge[2])
    total_cost+=edge[0]
    if max_cost < edge[0]:
      max_cost = edge[0]

print(total_cost - max_cost)
