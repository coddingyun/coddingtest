n = int(input())

graph = [[0]*n for _ in range(n)]

for i in range(n):
  graph[i][:i+1] = (list(map(int, input().split())))

for i in range(1, n):
  for j in range(n):
    graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]


print(max(graph[n-1]))
    