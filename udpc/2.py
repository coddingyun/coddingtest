import sys
input = sys.stdin.readline

str = list(input())[:-1]

u_score_min = 0
u_score_max = 0
d_score_min = 0
d_score_max = 0
p_score_min = 0
p_score_max = 0
c_socre_min = 0
c_socre_max = 0

for i in range(len(str)):
  if str[i] == 'U' or str[i] == 'C':
    u_score_max += 1
    c_socre_max += 1
  else:
    d_score_max += 1
    p_score_max += 1

# print(u_score, d_score, p_score)
check = 0
if d_score_max % 2 ==0:
  if u_score_max > d_score_max//2:
    print("U", end="")
    check += 1
else:
  if u_score_max > d_score_max//2+1:
    print("U", end="")
    check += 1
if d_score_max > u_score_min:
  print("D", end="")
  check += 1
if p_score_max > u_score_min:
  print("P", end="")
  check += 1

if check == 0:
  print("C", end="")
print()

