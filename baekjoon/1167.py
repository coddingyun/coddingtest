n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1) 
distance = [0]*(n+1)

for i in range(n):
  array = list(map(int, input().split()))[:-1]
  a = array[0]
  for j in range(1, len(array), 2):
    graph[a].append((array[j], array[j+1]))

def dfs(a, b):
  visited[a] = True
  for i in graph[a]:
    node, dist = i
    if visited[node] == False:
      distance[node] = max(distance[node], b+dist)
      dfs(node, max(distance[node], b+dist))

result = 0
idx = 1
dfs(1,0)
for i in range(1, n+1):
  if result < distance[i]:
    result = distance[i]
    idx = i

visited = [False]*(n+1) 
distance = [0]*(n+1)
dfs(idx,0)
print(max(distance))