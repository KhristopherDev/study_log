import random

choice = [1, 1, 1, 1, 1]
numbers = [1, 2, 3, 4, 5]
a = 0

while True:
  msg = input()

  while a != 4:
    j = random.randint(1,choice[a])
    if (j == choice[a]):
      print(f"Your number:  {numbers[a]}")
      if (numbers[a] == msg):
        if (choice[a]>1):
          choice[a]-=1
      else:
        choice[a]+=1
      a = 0
      break;
    else:
      a+=1
      if (a >= 4):
        a = 0