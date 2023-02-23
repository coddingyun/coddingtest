from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

array = list(map(int, input().split()))

def range_by_bisect(array, n):
  left_idx = bisect_left(array, n)
  right_idx = bisect_right(array, n)
  return right_idx - left_idx

result = range_by_bisect(array, x)
if result ==0:
  print(-1)
else:
  print(result)