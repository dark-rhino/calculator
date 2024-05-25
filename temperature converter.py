print(" _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)")


temperature = input("what is the temperature?\n")
unit = input("what is the unit? c= celcius,f= farenheit,k= kelvin\n")
unit2 =input("what is the unit you want to convert to?c,f,k\n")
if unit == "c" and unit2 == "f":
  print(int(temperature) * 9/5 + 32)
elif unit == "c" and unit2 == "k":
  print(int(temperature) + 273.15)
elif unit == "f" and unit2 == "c":
  print((int(temperature) - 32) * 5/9)
elif unit == "f" and unit2 == "k":
  print(int(temperature) * 5/9 + 273.15)
elif unit == "k" and unit2 == "c":
  print(int(temperature) - 273.15)
elif unit == "k" and unit2 == "f":
  print(int(temperature) * 9/5 - 459.67)
else: 
  print("invalid input")