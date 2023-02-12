import heapq

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

n, m = map(int, input().split())

parent = [0] * (n+1)
q = []

total_cost = 0
for _ in range(m):
  a, b, c = map(int, input().split())
  heapq.heappush(q, (c,a,b))
  total_cost+=c

for i in range(1, n+1):
  parent[i] = i

result_cost = 0
while q:
  cost, x, y = heapq.heappop(q)
  if find_parent(x, parent) != find_parent(y, parent):
    result_cost += cost
    union_parent(x, y, parent)

print(total_cost-result_cost)