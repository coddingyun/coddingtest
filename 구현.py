n = int(input())

count = (10+5)*60
count += (60-15)*15

if n>3:
  result = count*(n)+3600
else:
  result = count*n+1

print(result)

h = int(input())

result = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        result+=1
print(result)