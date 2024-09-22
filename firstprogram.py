num1 = int(input("enter 1num"))
num2 = int(input("enter 2num"))
num3 = int(input("enter 3num"))

if num1 == num2 and num2 == num3:
  print("All nums are equal")
elif num1 > num2 and num1 > num3:
  print("num1 is greater")
elif num2 > num1 and num2 > num3:
  print("num2 is greater")
elif num3 > num1 and num3 > num2:
  print("num3 is greater")
