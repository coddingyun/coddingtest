import heapq

n = int(input())

cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))

total = 0
while cards:
  if len(cards) == 1:
    break
  first = heapq.heappop(cards)
  second = heapq.heappop(cards)
  total += (first+second)
  heapq.heappush(cards, first+second)

print(total)