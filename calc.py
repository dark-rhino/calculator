print("hello,world")
number = float(input("enter a number\n"))
process = input("do you want to + , - , * , /\n")
number_1 = float(input("enter the number\n"))
if process == "+":
  print(number + number_1)
elif process == "-":
  print(number - number_1)
elif process == "*":
  print(number * number_1)
elif process == "/":
  print(number / number_1)