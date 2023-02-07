s = list(map(int, input()))

def multiply(x, y):
  return x*y

def sum(x, y):
  return x+y

result = s[0]

for i in range(1,len(s)):
  result = max(multiply(result, s[i]), sum(result, s[i]))

print(result)
  