import sys
input = sys.stdin.readline
n = int(input())

d_score = 0
p_score = 0

predict_list = []

for i in range(n):
  predict_list.append(input())

for i in range(n):
  if predict_list[i] == 'D\n':
    d_score += 1
  else:
    p_score += 1
  if abs(d_score-p_score) == 2:
    break

print(d_score, end="")
print(":", end = "")
print(p_score)