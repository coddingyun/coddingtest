import sys
input = sys.stdin.readline

n, k = map(int, input().split())

courses1 = []
courses2 = []
courses3 = []

for _ in range(n):
  a, b, c = map(int, input().split())
  courses1.append(a+b)
  courses2.append(a+c)
  courses3.append(b+c)


courses1.sort(reverse=True)
result1 = 0
for i in range(k):
  result1 += courses1[i]
courses2.sort(reverse=True)
result2 = 0
for i in range(k):
  result2 += courses2[i]
courses3.sort(reverse=True)
result3 = 0
for i in range(k):
  result3 += courses3[i]
  
print(max(result1, result2, result3))