n, m = list(map(int,input().split()))
array = list(map(int,input().split()))

#이건 분명 시간 초과를 받을 것이다. 높이가 최대 10억이기 때문이다.
result = max(array)-1

while True:
  sum = 0
  for i in array:
    if i>result:
      sum+=(i-result)
  if sum>=m:
    break
  result-=1

print(result)

start = 0
end = max(array)
result=0
while(start<=end):
  total = 0
  mid = (start+end)//2
  for i in array:
    if i>mid:
      total+=(i-mid)
  if total==m:
    result=mid
  elif total>m:
    result=mid
    start=mid+1
  else:
    end=mid-1

print(result)