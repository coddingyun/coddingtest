def binary_search(start, end, target):
  global array
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target:
      return True
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
  if binary_search(0, n-1, target):
    print(1, end=' ')
  else:
    print(0, end=' ')