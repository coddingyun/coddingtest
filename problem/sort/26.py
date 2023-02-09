import heapq

n = int(input())

array = []

for i in range(n):
  heapq.heappush(array, int(input()))

'''result = 0
prev = array[0]
array.pop(0)'''
#print(array)
result = 0

while len(array) > 1:
  one = heapq.heappop(array)
  two = heapq.heappop(array)
  total = one + two
  heapq.heappush(array, total)
  result += total

print(result)