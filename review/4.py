n = int(input())

coins = list(map(int, input().split()))
coins.sort(reverse = True)


for i in range(1, sum(coins)+2):
  price = i
  r=False
  for j in range(n):
    if coins[j]<=price:
      price -= coins[j]
      if price == 0:
        r = True
  if r == False:
    print(i)
    break