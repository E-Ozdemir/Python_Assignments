
# Task : Let's say; you left a message in the past that prints a password you need./
# To see the password you wrote, you need to enter your name and the program should recognize you.

name = 'emre'
user_name = str(input('Please write your first name: ')).lower()
if name == user_name:
  print('Hello,',name.capitalize(),'The password is:W@12')
else:
  print('Hello,',user_name.capitalize(),'See you later.')
