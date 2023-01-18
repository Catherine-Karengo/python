print("leap year or not APP")
print("--------------------")

for x in range(4):
  print("Enter any year")
  year = int(input())

  if year % 4 == 0:
    a = 1
  else:
    a = 0

  if year % 100 == 0:
    b = 0
  else:
    b = 1

  if year % 400 == 0:
    c = 0
  else:
    c = 1

  total = a+b+c

  if total == 1 or total == 3:
    print(str(year)+" is a leap year")
  else:
    print(str(year)+" is a not leap year")