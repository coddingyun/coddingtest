import heapq

n = int(input())

q = [1]
result = []
t=0

while t<=2000:
  now = heapq.heappop(q)
  result.append(now)
  heapq.heappush(q, now*2)
  heapq.heappush(q, now*3)
  heapq.heappush(q, now*5)
  t += 1


result = list(set(result))
result.sort()
print(result)
print(result[n-1])
  