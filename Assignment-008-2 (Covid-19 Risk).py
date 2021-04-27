age = input('Are you a cigarette addict older than 75 years old?').capitalize()
if age == 'Yes':
  age = True
else:
  age = False
chronic = input('Do you have a severe chronic disease? ').capitalize()
if chronic == 'Yes' :
  chronic = True
else:
  chronic = False
immune = input('Is your immune system too weak?').capitalize()
if immune == 'Yes' :
  immune = True
else:
  immune = False
if age and chronic and immune :
  print('You are in risky group')
else:
  print('You are not in risky group')
