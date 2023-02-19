import sys
input = sys.stdin.readline
n = int(input())

graph = [[0]*n for _ in range(n)]

def check_시간초과(graph, a, b):
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, 1, -1, -1, 1, 1, -1,]
  for i in range(8):
    nx, ny = a, b
    while nx >= 0 and nx<n and ny>=0 and ny<n:
      nx = nx + dx[i]
      ny = ny + dy[i]
      if nx >= 0 and nx<n and ny>=0 and ny<n and graph[nx][ny] == 1:
        return False
  return True

def check(graph, a, b):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 1 and (i!=a or j!=b):
        if abs(a-i) == abs(b-j) or b == j:
          return False
  return True


ans = 0
def n_queens(x):
  global ans
  if x == n:
    ans += 1
    return 
  else:
    for i in range(n):
      graph[x][i] = 1
      if check(graph, x, i):
        n_queens(x+1)
      graph[x][i] = 0

n_queens(0)
print(ans)
    