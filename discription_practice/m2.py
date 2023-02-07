N, M = map(int, input().split())
min_array = []
for i in range(N):
  data = list(map(int, input().split()))
  min_array.append(min(data))

result = max(min_array)

print(result)