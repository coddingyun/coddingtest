n = int(input())

#up = [i+1 for i in range(n)]
down = [0]
for i in range(n):
  down.append(int(input()))

first = []
second = []
answer = set()

def dfs(idx, first, second):
  first.add(idx)
  #print(idx)
  second.add(down[idx])
  if down[idx] in first:
    if first == second:
      #print(answer)
      answer.update(first)
    return
  return dfs(down[idx], first, second)

for i in range(n):
  if i+1 not in answer:
    dfs(i+1, set(), set())

print(len(answer))
answer = list(answer)
answer.sort()
for data in answer:
  print(data)
    