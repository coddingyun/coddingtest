n, c = map(int, input().split())

array = []

for i in range(n):
  array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]

while start <= end:
  mid = (start + end) // 2
  value = array[0]
  count = 1
  for i in range(n):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count < c:
      end = mid - 1
  else:
    start = mid + 1
    result = mid

print(result)