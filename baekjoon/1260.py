from collections import deque

n, m, k = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

result = []
visited = [False]*(n+1)

def dfs(a):
  visited[a] = True
  result.append(a)
  for i in graph[a]:
    if visited[i] == False:
      dfs(i)

result2 = []
visited2 = [False]*(n+1)

q = deque()
q.append(k)
visited2[k] = True
result2.append(k)

while q:
  now = q.popleft()
  for i in graph[now]:
    if visited2[i] == False:
      q.append(i)
      visited2[i]=True
      result2.append(i)

dfs(k)
for i in result:
  print(i, end= ' ')
print()
for i in result2:
  print(i, end=' ')

  