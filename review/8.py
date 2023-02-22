array = list(input())

alpha = []
digit = []

for data in array:
  if data.isalpha():
    alpha.append(data)
  else:
    digit.append(int(data))

alpha.sort()
result = "".join(alpha)
result += str(sum(digit))

print(result)