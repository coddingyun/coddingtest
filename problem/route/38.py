n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

array = [0] * (n+1)

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] != INF:
      array[i] += 1
      array[j] += 1 #여기서 i랑 j가 같아진 경우는 +2가 되니까

count = 0
for i in range(1, n+1):
  if array[i] == n+1:
    count += 1

print(count)