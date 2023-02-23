n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b= map(int, input().split())
  graph[a][b] = 0

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
#print(graph)
for i in range(1, n+1):
  r = True
  for j in range(1, n+1):
    if graph[i][j] == 0 or graph[j][i] == 0:
      continue
    else:
      r = False
      break
  if r == True:
    result += 1

print(result)