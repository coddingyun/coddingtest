from collections import deque
import sys
input = sys.stdin.readline

graph = ""

for _ in range(3):
  a, b, c = map(int, input().split())
  graph += str(a)
  graph += str(b)
  graph += str(c)

q = deque()
q.append(graph)

visited = {graph: 0} # 딕셔너리 형태 (그래프 모양: 최소 횟수)

target = "123456780"

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
  while q:
    ngraph = q.popleft()
    cnt = visited[ngraph]
    if ngraph == target:
      return cnt
    zero = ngraph.index('0') # 0이 위치해 있는 인덱스 값
    x = zero//3
    y = zero%3
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=0 and nx<3 and ny>=0 and ny<3:
        nzero = nx*3 + ny
        ngraph_list = list(ngraph)
        ngraph_list[zero], ngraph_list[nzero] = ngraph_list[nzero], ngraph_list[zero]
        str_ng_list = "".join(ngraph_list)
        if visited.get(str_ng_list, 0) == 0:
          visited[str_ng_list] = cnt + 1
          #print(visited)
          q.append(str_ng_list)
  return -1
print(bfs())