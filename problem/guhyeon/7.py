s = list(map(int, input()))

n = len(s)//2

left = sum(s[:n])
right = sum(s[n:])

if left == right:
  print("LUCKY")
else:
  print("READY")