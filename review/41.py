def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x], parent)
  return parent[x]

def union_parent(x,y,parent):
  x = find_parent(x, parent)
  y = find_parent(y, parent)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x

n, m = map(int, input().split())

graph = []
parent = [i for i in range(n+1)]
print(parent)


for i in range(n):
  graph.append(list(map(int, input().split())))

plans = list(map(int, input().split()))

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      if find_parent(i, parent) != find_parent(j, parent):
        union_parent(i, j, parent)

result = find_parent(plans[0])

r = True
for i in range(1, len(plans)):
  if result != find_parent(plans[i]):
    r = False

if r == True:
  print("YES")
else:
  print("NO")
      