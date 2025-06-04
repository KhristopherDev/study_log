import random

chances = [1, 1, 1]
gen = [1, 2, 3]
rndC = random.randint(0, len(chances)-1)
products = []
percentage = []
a = 0
j = 0
# option = input("Write a number between 1 and 5: ")
executions = input("Write a number of executions: ")
verif = True

while verif:
  try:
    # int(option)
    int(executions)
    # if int(option) > 5: raise Exception("Number too high! Choose between 1 and 5")
    verif = False
  except Exception as e:
    print(f"Can't convert string to number. Exception: {e}")
    # option = input("Write a number between 1 and 5: ")
    executions = input("Write a number of executions: ")
  

while True:
  option = input("Write a number between 1 and 3 (or write 'exit'): ")
  if option == 'exit':
    for i in range(5):
      percentage.append((products.count(i+1) / len(products)) * 100)
    print("Finished execution!")
    print(
      f"Your chosen Number: {option}\n"
      f"Executions: {executions}\n"
      f"Highest number present is: {percentage.index(max(percentage)) + 1} ({max(percentage):.2f}%)"
    )
    break
    
    
  verif = True
  while verif:
    try:
      int(option)
      if int(option) > len(chances)-1: raise Exception("Number too high! Choose between 1 and 5")
      verif = False
    except Exception as e:
      option = input("Write a number between 1 and 5: ")

  while j < int(executions):
    rndC = random.randint(0, len(chances)-1)
    if random.randint(1, 5) == 1:
      if chances[rndC] > 5: chances[rndC]-= 5
    while random.randint(1,chances[rndC]) <= chances[rndC]/10 <= chances[rndC]:
      rndC = random.randint(0, len(chances)-1)
    products.append(gen[rndC])
    if int(option) != int(gen[rndC]):
      if chances[rndC] > 50:
        chances[rndC]+=5
    else:
      if chances[rndC] > 5: chances[rndC]-=5
    j+=1
  j = 0
  print("I think your number in your mind is: " + str(gen[rndC]))