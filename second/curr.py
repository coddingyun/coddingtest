from collections import deque

n = int(input())

times = []
graph = [[] for _ in range(n)]
indegree = [0]*n
answer = [0]*n

for i in range(n):
  arr = list(map(int, input().split()))
  times.append(arr[0])
  for j in range(1, len(arr)-1):
    graph[arr[j]-1].append(i)
    indegree[i] += 1
q = deque()

for i in range(n):
  if indegree[i] == 0:
    q.append(i)
    answer[i] = times[i]

while q:
  now = q.popleft()
  for i in graph[now]:
    answer[i] = answer[now] + times[i]
    indegree[i] -= 1
    if indegree[i] == 0:
      q.append(i)

for ans in answer:
  print(ans)