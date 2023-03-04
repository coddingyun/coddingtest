import heapq

n = int(input())

cards = []

for _ in range(n):
  heapq.heappush(cards, int(input()))
  #cards.append(int(input()))
answer = 0

while len(cards) > 1:
  first = heapq.heappop(cards)
  second = heapq.heappop(cards)
  answer += first+second
  heapq.heappush(cards, first+second)

print(answer)