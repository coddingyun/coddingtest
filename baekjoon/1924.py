m, d = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(2, 13):
  days[i] += days[i-1]

total_days = days[m-1] + d

remainder = total_days % 7

if remainder == 1:
  print("MON")
if remainder == 2:
  print("TUE")
if remainder == 3:
  print("WED")
if remainder == 4:
  print("THU")
if remainder == 5:
  print("FRI")
if remainder == 6:
  print("SAT")
if remainder == 0:
  print("SUN")