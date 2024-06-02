import time


def clear_line(): 
  for i in range(80): 
      print("\b")


clear_line
print('''\033[1;37;40m _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)\n ''',  end="")
time.sleep(3)
choice = input('''\033[2;32;40m DO YOU WANT CALCULATE TIP,OR DO SOME MATHS, OR CONVERT THE LENGTH UNIT OR CONVERT TEMPERATURE OR ENERGY CONVERTER OR CONVERT TIME\n''')
if choice == "TIP":
  #If the bill was $150.00, split between 5 people, with 12% tip.
  total = input("how much the total amount is?\n")
  #Each person should pay (150.00 / 5) * 1.12 = 33.6
  dollar = (input("how much percentage do you want to give?\n"))
  tip = int(total) / 100 * int(dollar)
  persons = int(input("how many people are there?\n"))
  persons_in_int = int(persons)
  tip_in_int = int(tip)
  amount = (tip / persons_in_int )
  amount_1 = round(amount)
  print(f"the amount each person should give {amount_1}")
elif choice == "maths":
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
  else:
    print("invalid choice")
  
elif choice == "length":
    unit = (input("what unit you want convert from? inch, foot,\nkilometer,meter, centimeter, millimeter.\n"))
    unit2 = (input("which unit you want to convert to?inch, foot,\nkilometer,meter,centimeter, millimeter.\n"))
    value = float(input(f"enter the value of {unit}\n"))
    if unit == "inch" and unit2 == "foot" :
      print(value/12)
    elif unit == "inch" and unit2 == "kilometer":
      print(value/39370)
    elif unit == "inch" and unit2 == "meter":
      print(value/39.37)
    elif unit == "inch" and unit2 == "centimeter":
      print(value*2.54)
    elif unit == "inch" and unit2 == "millimeter":
      print(value*25.4)
    elif unit == "foot" and unit2 == "inch":
      print(value*12)
    elif unit == "foot" and unit2 == "kilometer":
      print(value/3281)
    elif unit == "foot" and unit2 == "meter":
      print(value/3.281)
    elif unit == "foot" and unit2 == "centimeter":
      print(value*30.48)
    elif unit == "foot" and unit2 == "millimeter":
      print(value*304.8)
    elif unit == "killometer" and "unit2" == "inch":
      print(value*39370)
    elif unit == "killometer" and "unit2" == "foot":
      print(value*3281)
    elif unit == "killometer" and  unit2 == "meter":
      print(value*1000)
    elif unit == "killometer" and unit2 == "centimeter":
      print(value*100000)
    elif unit == "killometer" and unit2 == "millimeter":
      print(value*10**6)
    elif unit == "meter" and unit2 == "inch":
      print(value*39.37)
    elif unit == "meter" and unit2 == "foot":
      print(value*3.281)
    elif unit == "meter" and unit2 == "kilometer":
      print(value/1000)
    elif unit == "meter" and unit2 == "centimeter":
      print(value*100)
    elif unit == "meter" and unit2 == "millimeter":
      print(value*1000)
    elif unit == "centimeter" and unit2 == "inch":
      print(value/2.54)
    elif unit == "centimeter" and unit2 == "foot":
      print(value/30.48)
    elif unit == "centimeter" and unit2 == "kilometer":
      print(value/100000)
    elif unit == "centimeter" and unit2 == "meter":
      print(value/100)
    elif unit == "centimeter" and unit2 == "millimeter":
      print(value*10)
    elif unit == "millimeter" and unit2 == "inch":
      print(value/25.4)
    elif unit == "millimeter" and unit2 == "foot":
      print(value/304.8)
    elif unit == "millimeter" and unit2 == "kilometer":
      print(value/10**6)
    elif unit == "millimeter" and unit2 == "meter":
      print(value/1000)
    elif unit == "millimeter" and unit2 == "centimeter":
      print(value/10)
    else:
      print("invalid unit")
elif choice == "TEMPERATURE":
  temperature = input("what is the temperature?\n")
  unit = input("what is the unit? c,f,k\n")
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

elif choice == "energy":
  energy = int(input("what is value of the energy?"))
  unit = input(("what is the unit?"))
  unit2 = input(("what is the unit you want to convert to?"))
  if unit == "joule" and unit2 == "kilojoule":
    print(energy / 1000)
  elif unit == "joule" and unit2 == "gram calorie":
    print(energy / 4.184)
  elif unit == "joule" and unit2 == "kilocaloir":
    print(energy / 4184)
  elif unit == "joule" and unit2 == "watt hour":
    print(energy / 3600)
  elif unit == "joule" and unit2 == "killowatt hour":
    print(energy / 0.0000036 )
  elif unit == "joule" and unit2 == "electronvolt":
    print(energy * 6.242*10**18 )
  elif unit == "joule" and unit2 == "british thermal unit":
    print(energy / 1055)
  elif unit == "joule" and unit2 == "us therm":
    print(energy / 1.055*10**8)
  elif unit == "joule" and unit2 == "foot pound":
    print(energy /  1.356)
  elif unit == "kilowatt hour" and unit2 == "joule":
    print(energy * 3.6*10**6)
  elif unit == "kilowatt hour" and unit2 == "kilojoule":
    print(energy * 3600)
  elif unit == "kilowatt hour" and unit2 == "gramcalorie":
    print(energy * 860421)
  elif unit == "kilowatt hour" and unit2 == "kilocalorie":
    print(energy * 860.4)
  elif unit == "kilowatt hour" and unit2 == "watt hour":
    print(energy * 1000)
  elif unit == "kilowatt hour" and unit2 == "electronvolt":
    print(energy * 2.247*10**25)
  elif unit == "kilowatt hour" and unit2 == "british thermal unit":
    print(energy * 3412.14)
  elif unit == "kilowatt hour" and unit2 == "us therm":
    print(energy*29.3)
  elif unit == "kilowatt hour" and unit2 == "foot pound":
    print(energy * 2.655*10**6)
  elif unit == "kilojoule" and unit2 == "kilowatt hour":
    print(energy / 3600)
  elif unit == "kilojoule" and unit2 == "joule":
    print(energy*1000)
  elif unit == "kilojoule" and unit2 == "gram calorie":
    print(energy * 239.006)
  elif unit == "kilojoule" and unit2 == "kilo calorie":
    print(energy / 4.184)
  elif unit == "kilojoule" and unit2 == "watt hour":
    print(energy / 3.6)
  elif unit == "kilojoule" and unit2 == "kilowatt hour":
    print(energy / 3600)
  elif unit == "kilojoule" and unit2 == "electronvolt":
    print(energy * 6.242*10**18)
  elif unit == "kilojoule" and unit2 == "british thermal unit":
    print(energy / 1.055)
  elif unit == "kilojoule" and unit2 == "us therm":
    print(energy / 105500)
  elif unit == "kilojoule" and unit2 == "foot pound":
    print(energy * 737.562)
  elif unit == "gram calorie" and unit2 == "joule":
    print(energy*4.184)
  elif unit == "gram calorie" and unit2 == "kilojoule":
    print(energy / 239)
  elif unit == "gram calorie" and unit2 == "kilocalorie":
    print(energy / 1000)
  elif unit == "gram calorie" and unit2 == "watt hour":
    print(energy / 860.4)
  elif unit == "gram calorie" and unit2 == "kilowatt hour":
    print(energy / 860400)
  elif unit == "gram calorie" and unit2 == "electronvolt":
    print(energy * 2.61*10**19 )
  elif unit == "gram calorie" and unit2 == "british thermal unit":
    print(energy / 252.2)
  elif unit == "gram calorie" and unit2 == "us therm":
    print(energy / 2.521*10**7)
  elif unit == "gram calorie" and unit2 == "footpound":
    print(energy * 3.08596)
  elif unit == "kilocalorie" and unit2 == "joule":
    print(energy * 4184)
  elif unit == "kilocalorie" and unit2 == "kilojoule":
    print(energy * 4.184 )
  elif unit == "kilocalorie" and unit2 == "gram calorie":
    print(energy *1000)
  elif unit == "kilocalorie" and unit2 == "kilo calorie ":
    print(energy / 1000)
  elif unit == "kilocalorie" and unit2 == "watt hour":
    print(energy / 860.4)
  elif unit == "kilocalorie" and unit2 == "kilowatt hour":
    print(energy / 860400)
  elif unit == "kilocalorie" and unit2 == "electronvolt":
    print(energy * 2.611*10**19)
  elif unit == "kilocalorie" and unit2 == "british thermal unit":
    print(energy / 252.2)
  elif unit == "kilocalorie" and unit2 == "us therm":
    print(energy / 2.521*10**7)
  elif unit == "kilocalorie" and unit2 == "foot pound":
    print(energy * 3.08596)
  elif unit == "watt hour" and unit2 == "joule":
    print(energy * 3600)
  elif unit == "watt hour" and unit2 == "kilojoule":
    print(energy * 3.6)
  elif unit == "watt hour" and unit2 == "gram calorie":
    print(energy * 860.421)
  elif unit == "watt hour" and unit2 == "kilo calorie":
    print(energy / 1.162)
  elif unit == "watt hour" and unit2 == "kilowatt hour":
    print(energy / 1000)
  elif unit == "watt hour" and unit2 == "electronvolt":
    print(energy * 2.247 * 10**22)
  elif unit == "watt hour" and unit2 == "british thermal unit":
    print(energy * 3.41214)
  elif unit == "watt hour" and unit2 == "us therm":
    print(energy *29300)
  elif unit == "watt hour" and unit2 == "foot pound":
    print(energy * 2655.22)
  elif unit == "kilowatt hour" and unit2 == "joule":
    print(energy * 3.6*10**6)
  elif unit == "kilowatt hour" and unit2 == "kilojoule":
    print(energy * 3600)
  elif unit == "kilowatt hour" and unit2 == "gram calorie":
    print(energy * 860421)
  elif unit == "kilowatt hour" and unit2 == "kilo calorie":
    print(energy * 860.421)
  elif unit == "kilowatt hour" and unit2 == "watt hour":
    print(energy * 1000)
  elif unit == "kilowatt hour" and unit2 == "eletronvolt":
    print(energy*2.247*10**25)
  elif unit == "kilowatt hour" and unit2 == "british thermal unit":
    print(energy * 3412.14)
  elif unit == "kilowatt hour" and unit2 == "us therm":
    print(energy / 29.3)
  elif unit == "kilowatt hour" and unit2 == "foot pound":
    print(energy * 2.655 * 10 **6)
  elif unit == "electronvolt" and unit2 == "joule":
    print(energy / 6.242*10**18)
  elif unit == "electronvolt" and unit2 == "kilojoule":
    print(energy / 6.242*10**21)
  elif unit == "electronvolt" and unit2 == "gram calorie":
    print(energy/ 2.611*10**19)
  elif unit == "electronvolt" and unit2 == "kilo calorie":
    print(energy / 2.611*10**22)
  elif unit == "electronvolt" and unit2 == "watt hour":
    print(energy / 2.247*10**22)
  elif unit == "electronvolt" and unit2 == "kilowatt hour":
    print(energy / 2.247*10**25)
  elif unit == "electronvolt" and unit2 == "british thermal unit":
    print(energy / 6.585*10**21)
  elif unit == "electronvolt" and unit2 == "us therm":
    print(energy / 6.584*10**26)
  elif unit == "electronvolt" and unit2 == "foot pound":
    print(energy/8.462*10**18)
  elif unit == "british thermal unit" and unit2 == "joule":
    print(energy * 1055.06)
  elif unit == "british thermal unit" and unit2 == "kilo joule":
    print(energy * 1.055)
  elif unit == "british thermal unit" and unit2 == "gram calorie":
    print(energy *252.164)
  elif unit == "british thermal unit" and unit2 == "kilo calorie":
    print(energy /3.966)
  elif unit == "british thermal unit" and unit2 == "watt hour":
    print(energy / 3.412)
  elif unit == "british thermal unit" and unit2 == "kilowatt hour":
    print(energy / 3412.14)
  elif unit == "british thermal unit" and unit2 == "electronvolt":
    print(energy * 6.585*10**21)
  elif unit == "british thermal unit" and unit2 == "us therm":
    print(energy / 99980)
  elif unit == "british thermal unit" and unit2 == "foot pound":
    print(energy * 778.169)
  elif unit == "us therm" and unit2 == "joule":
    print(energy * 1.055*10**8)
  elif unit == "us therm" and unit2 == "kilo joule":
    print(energy * 105480)
  elif unit == "us therm" and unit2 == "gram calorie":
    print(energy * 2.521*10**7)
  elif unit == "us therm" and unit2 == "kilo calorie":
    print(energy * 25210.4)
  elif unit == "us therm" and unit2 == "watt hour":
    print(energy * 29300.1)
  elif unit == "us therm" and unit2 == "kilowat hour":
    print(energy * 29.3 )
  elif unit == "us therm" and unit2 == "electronvolt":
    print(energy * 6.584*10**26)
  elif unit == "us therm" and unit2 == "british thermal unit":
    print(energy * 99976.1)
  elif unit == "us therm" and unit2 == "foot pound":
    print(energy * 7.78*10**7)
  elif unit == "foot pound" and unit2 == "joule":
    print(energy * 1.35582)
  elif unit == "foot pound" and unit2 == "kilo joule":
    print(energy / 737.6)
  elif unit == "foot pound" and unit2 == "gram calorie":
    print(energy / 3.086)
  elif unit == "foot pound" and unit2 == "kilo calorie":
    print(energy /3086)
  elif unit == "foot pound" and unit2 == "watt hour":
    print(energy / 2655)
  elif unit == "foot pound" and unit2 == "kilowatt hour":
    print(energy / 2.655*10**6)
  elif unit == "foot pound" and unit2 == "electronvolt":
    print(energy / 8.462*10**18)
  elif unit == "foot pound" and unit2 == "british thermal unit":
    print(energy / 778.2)
  elif unit == "foot pound" and unit2 == "us therm": 
    print(energy / 7.78*10**7)
  else:
    print("invalid input")


elif choice == "time":

  time = (int(input("what is the duration?\n")))
  unit = input("what is the unit?")
  unit2 = input("what is the unit you want to convert to?\n")
  if unit == "second" and unit2 == "minute":
    print(time / 60)
  elif unit == "milliseconds" and unit2 == "minute":
    print(time / 60000)
  elif unit == "hours" and unit2 == "minute":
    print(time * 60)
  elif unit == "days" and unit2 == "minute":
    print(time * 1440)
  elif unit == "week" and unit2 == "minute":
    print(time *10080)
  elif unit == "second" and unit2 == "milliseconds":
    print(time * 1000)
  elif unit == "minutes" and unit2 == "milliseconds":
    print(time * 60000)
  elif unit == "hours" and unit2 == "milliseconds":
    print(time * 3600000)
  elif unit == "days" and unit2 == "milliseconds":
    print(time * 86400000)
  elif unit == "week" and unit2 == "milliseconds":
    print(time * 604800000)
  elif unit == "seconds" and unit2 == "hours":
    print(time / 3600)
  elif unit == "minutes" and unit2 == "hours":
    print(time / 60)
  elif unit == "days" and unit2 == "hours":
    print(time / 24)
  elif unit == "week" and unit2 == "hours":
    print(time * 168)
  elif unit == "seconds" and unit2 == "days":
    print(time / 86400)
  elif unit == "minutes" and unit2 == "days":
    print(time /1440)
  elif unit == 'hours' and unit2 == "days":
    print(time / 24)
  elif unit == "week" and unit2 == "days":
    print(time *7)
  elif  unit == "seconds" and unit2 == "week":
    print(time / 604800)
  elif unit == "minutes" and unit2 == "week":
    print(time / 10080)
  elif unit == "hours" and unit2 == "week":
    print(time /168)
  elif unit == "days" and unit2 == "week":
    print(time / 7)
  elif unit == "milliseconds" and unit2 == "seconds":
    print(time / 1000)
  elif unit == "minutes" and unit2 == "seconds":
    print(time / 60)
  elif unit == "hours" and unit2 == "seconds":
    print(time * 3600)
  elif unit == "days" and unit2 == "seconds":
    print(time * 86400)
  elif unit == "week" and unit2 == "seconds":
    print(time * 604800)
  elif unit == "milliseconds" and unit2 == "minutes":
    print(time / 60000)
  elif unit == "seconds" and unit2 == "minutes":
    print(time / 60)
  elif unit == "hours" and unit2 == "minutes":
    print(time * 60)
  elif unit == "days" and unit2 == "minutes":
    print(time *1440)
  elif unit == "week" and unit2 == "minutes":
    print(time * 10080)
  elif unit == "milliseconds" and unit2 == "hours":
    print(time / 3600000)
  elif unit == "seconds" and unit2 == "hours":
    print(time / 3600)
  elif unit == "minutes" and unit2 == "hours":
    print(time / 60)
  elif unit == "days" and unit2 == "hours":
    print(time / 24)
  elif unit == "week" and unit2 == "hours":
    print(time * 168)
  else:
    print("invalid choice")


else:
  print("invalid choice")