s = list(input())

zero = s.count('0')/2
one = s.count('1')/2

while zero>0:
  for i in range(len(s)-1,-1,-1):
    if s[i] == '0':
      s[i:] = s[i+1:]
      break
  zero -= 1

while one > 0:
  for i in range(len(s)):
    if s[i] == '1':
      s[i:] = s[i+1:]
      break
  one -= 1

print("".join(s))