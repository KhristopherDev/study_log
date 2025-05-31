import random

chances = [1, 1, 1, 1, 1]
gen = [1, 2, 3, 4, 5]
products = []
percentage = []
a = 0
j = 0
option = input("Write a number between 1 and 5: ")
executions = input("Write a number of executions: ")
verif = True

while verif:
  try:
    int(option)
    int(executions)
    if int(option) > 5: raise Exception("Number too high! Choose between 1 and 5")
    verif = False
  except Exception as e:
    print(f"Can't convert string to number. Exception: {e}")
    print("Write a number!")
    option = input("Write a number between 1 and 5: ")
    executions = input("Write a number of executions: ")
  

while j < int(executions):
  rndC = random.randint(0, 4)
  while random.randint(1,chances[rndC]) != 1:
    rndC = random.randint(0, 4)
  print("I think your number is: " + str(gen[rndC]))
  products.append(gen[rndC])
  if int(option) != int(gen[rndC]):
    chances[rndC]+=chances[rndC]*1000
  else:
    if chances[rndC] > chances[rndC]*1000: chances[rndC]-= chances[rndC]*999
  j+=1

for i in range(5):
  percentage.append((products.count(i+1) / len(products)) * 100)


print("Finished execution!")
print(
  f"Your chosen Number: {option}\n"
  f"Executions: {executions}\n"
  f"Highest number present is: {percentage.index(max(percentage)) + 1} ({max(percentage):.2f}%)"
)