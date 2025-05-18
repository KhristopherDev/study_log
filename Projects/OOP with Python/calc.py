class operation:
  def __init__(self, operation):
    try:
      self.operation = int(eval(operation))
    except ValueError as e:
      self.operation = e
  def __str__(self):
    return f"{self.operation if isinstance(self.operation, int) else f"Erro ao calcular a expressão, tente outro valor. \n Error found: {self.operation}"}"
  
print("Calculadora")
while True:
  calc = operation(input("⨘:"))
  print(calc)
