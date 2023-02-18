from collections import deque

n, m = map(int, input().split())

def check(a):
  if a>=0 and a<=100000:
    return True
  else:
    return False

distance = [0]*(100001)
q = deque()
q.append(n)

while q:
  now = q.popleft()
  if check(now+1) and distance[now+1] == 0:
    q.append(now+1)
    distance[now+1] = distance[now] + 1
  if check(now-1)and distance[now-1] == 0:
    q.append(now-1)
    distance[now-1] = distance[now] + 1
  if check(now*2) and distance[now*2] == 0:
    q.append(now*2)
    distance[now*2] = distance[now] + 1

if n == m:
  print(0)
else:
  print(distance[m])