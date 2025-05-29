from googlesearch import search as s
import os
result = []

def Search(mySearch):
  for i in mySearch:
    if 'https' in i or 'http' in i:
      result.append(i)
  if len(result) > 0:
    print(f"Oops, your password has been found in these websites:")
    for x in result:
      print(x)
  else:
    print("Congratulations! Your password is secure and is not present in any website!")
  

while True:
  Search(s(input("What password you want to search?: "), num_results=10, safe=None, ssl_verify=None))
  if input("Exit? (Y/N)") == "Y":
    break
  else:
    result = []
    os.system('cls' if os.name == '' else 'clear')
    