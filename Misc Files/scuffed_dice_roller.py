import random

result = 0

while True:
  try:
    print('How many dice would you like to roll?')
    num = int(input())
  except:
    print('Please try again...')
    continue

  try:
    print('How many sides for each die?')
    sides = int(input())
  except:
    print('Please try again...')
    continue

  if num < 1 or sides < 1:
    print('Please try again...')
    continue

  for num in range(num, 0, -1):
    roll = random.randInt(1, sides)
    result += roll
    print(roll)

  print('The result is ' + str(result))
  print('')