from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

lists = [i+1 for i in range(n)]

combi_lists = list(permutations(lists,n))

b_answer = []
c_answer = []

def back_tr(i, b_ans, c_ans, visited):
  a = b_ans[i]
  c_ans.append(i+1)
  if len(c_ans) == n:
    return
  if i+a < n and i+a>=0 and visited[i+a] == False:
    visited[i+a] = True
    back_tr(i+a, b_ans, c_ans, visited)
  if i-a < n and i-a>=0 and visited[i-a] == False:
    visited[i-1] = True
    back_tr(i-a, b_ans, c_ans, visited)
  c_ans.pop()

for combi in combi_lists:
  b_answer = combi
  for i in range(n):
    c_answer = []
    visited = [False]*n
    back_tr(i, b_answer, c_answer, visited)
    if len(c_answer) == n:
      break
  if len(c_answer) == n:
    break

if len(c_answer) == n:
  print("YES")
  for i in range(n):
    print(b_answer[i], end=" ")
  print()
  for i in range(n):
    print(c_answer[i], end=" ")
  print()
else:
  print("NO")