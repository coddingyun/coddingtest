# 입력값이 다음과 같이 들어온다
# 4
# AB BA CC DD

from collections import deque

n = int(input())

arr = list(input().split())

arr = "".join(arr)

def target(str, N):
  for i in range(0, N*2, 2):
    if str[i] != str[i+1]:
      return False
  return True

visited = set()
visited.add(arr)

q = deque()
q.append([arr, 0])

answer = -1

while q:
  narr, cnt = q.popleft()
  if target(narr, n):
    answer = cnt
    print(narr)
    break
  for i in range(n*2-1):
    tarr = list(narr)
    tarr[i], tarr[i+1] = tarr[i+1], tarr[i]
    if "".join(tarr) not in visited:
      visited.add("".join(tarr))
      q.append(["".join(tarr), cnt+1])

print(answer)
  