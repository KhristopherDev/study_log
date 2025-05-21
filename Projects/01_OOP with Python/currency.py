import requests
import tkinter as tk

root = tk.Tk()
root.title("Conversor de moedas")

label = tk.Label(root, text="Digite o valor em BRL:", font=("Arial", 18))
label.pack(padx=100, pady=20)

valor = tk.Text(root, width=30, height=1, font=("Arial", 16))
valor.pack()

buttonframe = tk.Frame(root)
for a in range(2):
    buttonframe.columnconfigure(a, weight=1)

btn1 = tk.Button(buttonframe, text="USD", font=("Arial", 12))
btn2 = tk.Button(buttonframe, text="EUR", font=("Arial", 12))
btn3 = tk.Button(buttonframe, text="BTC", font=("Arial", 12))

btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=20, pady=20)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=20, pady=20)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20, pady=20)

buttonframe.pack()

def get_exchange_rate(base='BRL', target='USD'):
    url = f"https://economia.awesomeapi.com.br/json/last/{base}-{target}"
    response = requests.get(url)
    data = response.json()
    return data[f'{base}{target}']['high']

def main():
    print("=== Conversor de Moedas ===")
    moeda_destino = input("Converter para (USD, EUR, BTC): ").upper()

    try:
        taxa = get_exchange_rate('BRL', moeda_destino)
        convertido = float(valor) * float(taxa)
        print(f"{valor:.2f} BRL = {convertido:.2f} {moeda_destino}")
    except Exception as e:
        print("Erro ao obter cotação:", e)

root.mainloop()

