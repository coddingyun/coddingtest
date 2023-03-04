from collections import deque

n, k = map(int, input().split())

arr = list(input().split())

target = sorted(arr)

visited = set()
visited.add("".join(arr))
q = deque()
q.append([arr, 0])

answer = -1
while q:
  narr, cnt = q.popleft()
  if narr == target:
    answer = cnt
    break
  for i in range(n-k+1):
    r = narr[i:i+k]
    r.reverse()
    r = narr[:i] + r + narr[i+k:]
    #print(r)
    if "".join(r) not in visited:
      visited.add("".join(r))
      q.append([r, cnt+1])

print(answer)