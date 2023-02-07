N = int(input())
store = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))

store.sort()
request.sort()

min=0
j=0
while True:
  if j==M:
    break
  if min>=N:
    print("no" ,end=' ')
    j+=1
  elif store[min]==request[j]:
    print("yes",end=' ')
    j+=1
  elif store[min]<request[j]:
    min+=1
  else:
    print("no",end=' ')
    j+=1

data = [0]*1000001
for i in range(N):
  data[store[i]]+=1

for j in range(M):
  if data[request[j]]>=1:
    print("yes", end=" ")
  else:
    print("no", end=' ')