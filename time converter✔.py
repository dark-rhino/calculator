print('''\033[2;32;40m _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)\n''')

time = int(input("what is the duration?\n"))
unit = input("what is the unit?\n")
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