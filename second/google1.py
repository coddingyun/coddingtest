from itertools import combinations

for _ in range(int(input())):
  # s = "".join(list(input().split()))
  s = list(map(int, input()))
  x = int(input())

def two_digit(numbers, lengs):
  total = 0
  for i in range(lengs):
    total += numbers[i]*(2**(lengs-i-1))
  return total

length = 1
answer = 0
while True:
  r = False
  candidates = list(combinations(s, length))
  #print(candidates)
  can_length = len(candidates)
  for i in range(can_length):
    if candidates[i][0] == 1:
      #print("h")
      if two_digit(candidates[i], len(candidates[i])) <= x:
        answer = length
        r = True
  if r==False:
    break
  length += 1
    

print(answer)
  