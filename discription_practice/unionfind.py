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

for i in range(1,n+1):
  parent[i]=i

for i in range(m):
  a, b, c = map(int, input().split())
  if a == 0:
    if parent[b] != parent[c]:
      union_set(b,c)

  elif a == 1:
    if find_parent(b) == find_parent(c):
      print("YES")
    else:
      print("NO")