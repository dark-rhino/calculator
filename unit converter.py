print("hello welcome to unit converter")
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
                