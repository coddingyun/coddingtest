array = [2,1,3,5,6,4,7,8,9]

# 선택정렬
for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[j] < array[min_index]:
      min_index = j

  array[i], array[min_index] = array[min_index], array[i]

print(array)

#삽입정렬
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)

#퀵정렬
def quick_sort(array, start, end):
  if start>=end:
    return
  pivot = start
  left=start+1
  right=end
  while left<=right:
    while left<=end and array[left]<=array[pivot]:
      left+=1
    while right>start and array[right]>=array[pivot]:
      right+=1
    if left>right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start,right-1)
  quick_sort(array,right+1, end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬의 장점을 살린 퀵정렬
def quick_sort2(array):
  if len(array) <= 1:
    return array

  pivot=array[0]
  tail=array[1:]

  left_side = [x for x in tail if x<=pivot]
  right_side = [x for x in tail if x>pivot]

  return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

print(quick_sort2(array))

#계수정렬
count = [0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1

for j in range(len(count)):
  for k in range(count[j]):
    print(count[j], end= " ")

#파이썬 라이브러리
result=sorted(array)
print(result)

array.sort()
print(array)