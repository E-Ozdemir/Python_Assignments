###ARMSTRONG NUMBER####
x = input('Write a positive number: ')
y =len(x)
summ = 0
while not x.isdigit():  # Checks if a digit number or not
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
  x = input("Type your age correctly:")
for i in range(y):
  summ = summ + (int(x[i]))**y
if summ == int(x):
  print (x,' is an Armstrong number')
else:
  print(x,' is not an Armstrong number')
