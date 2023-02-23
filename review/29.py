import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = []

for _ in range(n):
  houses.append(int(input()))

houses.sort()
start = 1 # 가능한 최소거리
end = houses[-1] - houses[0] #가능한 최대거리
result = 0
while start <= end:
  mid = (start+end)//2
  check = houses[0]
  cnt = 1
  for i in range(n):
    if houses[i] >= check + mid:
      cnt += 1
      check = houses[i]
  if cnt >= c:
    start = mid + 1
    result = max(result, mid)
  else:
    end = mid - 1

print(result)