print(''' _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)''')
energy = int(input("what is value of the energy?"))
unit = input(("what is the unit?"))
unit2 = input(("what is the unit you want to convert to?"))
if unit == "joule" and unit2 == "kilojoule":
  print(energy / 1000)
elif unit == "joule" and unit2 == "gram calorie":
  print(energy / 4.184)
elif unit == "joule" and unit2 == "kilocaloire":
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
