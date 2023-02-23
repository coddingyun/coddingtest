n = int(input())

numbers = list(map(int, input().split()))

operators = list(map(int, input().split()))
max_num = -int(1e9)
min_num = int(1e9)
def func (pre, cnt):
  global max_num, min_num, numbers, operators
  if cnt == n:
    max_num = max(max_num, pre)
    min_num = min(min_num, pre)
    return
  for i in range(4):
    if operators[i] != 0:
      operators[i] -= 1
      if i == 0:
        func(pre+numbers[cnt], cnt+1)
      if i == 1:
        func(pre-numbers[cnt], cnt+1)
      if i == 2:
        func(pre*numbers[cnt], cnt+1)
      if i == 3:
        if pre < 0:
          func(int(abs(pre)//numbers[cnt])*(-1), cnt+1)
        else:
          func(int(pre//numbers[cnt]), cnt+1)
      operators[i] += 1

func(numbers[0], 1)
print(max_num)
print(min_num)