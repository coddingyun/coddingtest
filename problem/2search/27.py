n, x = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = n-1

mid = 0
r = False

while start <= end:
  mid = (start+end) // 2
  if (mid==0 or array[mid-1]<x) and x == array[mid]:
    r = True
    break
  elif x > array[mid]:
    start = mid + 1
  else:
    end = mid - 1

start = 0
end = n-1
mid2 = 0
r2 = False

while start <= end:
  mid2 = (start+end) // 2
  if (mid2==n-1 or array[mid2+1]>x) and x == array[mid2]:
    r2 = True
    break
  elif x >= array[mid2]:
    start = mid2 + 1
  else:
    end = mid2 - 1

if r == False and r2 == False:
  print(-1)
else:
  print(mid2-mid+1)


from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)
    