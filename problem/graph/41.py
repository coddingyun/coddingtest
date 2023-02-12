n, m = map(int, input().split())

parent = [0] * (n+1)

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

target = list(set(list(map(int, input().split()))))

def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x], parent)
  return parent[x]

def union_parent(x, y, parent):
  x = parent[x]
  y = parent[y]
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for i in range(n):
  parent[i] = i
#print(parent)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      if find_parent(i, parent) != find_parent(j, parent):
        union_parent(i, j, parent)

#print(parent)
result = parent[target[0]-1]
r = True

for i in range(1,len(target)):
  if parent[target[i]-1] != result:
    r = False
    break

if r:
  print('YES')
else:
  print('NO')