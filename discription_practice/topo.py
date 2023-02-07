from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [0] *(n+1)

for i in range(1, n+1):
  data = list(map(int, input().split()))
  time[i] = data[1]
  for x in data[1:-1]:
    indegree[i]+=1
    graph[i].append(x)

result = copy.deepcopy(time) #리스트 복사
q = deque()
for i in range(1, n+1):
  if indegree[i] == 0:
    q.append(i)

#total_time = 0
while q:
  now = q.popleft()
  #total_time+=time[now]
  for i in graph[now]:
    indegree[i]-=1
    result[i]=max(result[i], result[now]+time[i])
    if (indegree[i]==0):
      q.append(i)

for i in range(1, n+1):
  print(result[i])