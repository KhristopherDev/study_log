import requests
import tkinter as tk

class Window: #Tkinter window encapsulation to use functions
    def __init__(self): # Window init
        self.entryValue = 0 # Set to 0 to prevent bugs
        self.target = "USD" # Default conversion value as USD

        self.root = tk.Tk() # root (window) of project
        self.root.title("Conversor de moedas") # Project Title

        self.label = tk.Label(
            self.root, text="Digite o valor em BRL:", font=("Arial", 18) # Top label
        )
        self.label.pack(padx=100, pady=10) # Packing of objects that can be set a padding in X and Y axis

        self.conversion = tk.Label(self.root, text='', font=("Arial", 18)) # Response label, initially set to empty value. This label is related to the main() function on line 66 and 69.
        self.conversion.pack(padx=100)

        self.entry = tk.Entry(self.root, width=30, font=("Arial", 16)) # Value entry. This object is related to self.entryValue in main() function on line 63, 66 and 67
        self.entry.pack()

        self.buttonframe = tk.Frame(self.root) # Buttons grid
        for a in range(2): # For loop in case of adding more options
            self.buttonframe.columnconfigure(a, weight=1)

        self.btn1 = tk.Button( # This button is rendered pressed
            self.buttonframe,
            text="USD",
            font=("Arial", 12),
            command=lambda: self.toggle(self.btn1),
        )
        self.btn2 = tk.Button(
            self.buttonframe,
            text="EUR",
            font=("Arial", 12),
            command=lambda: self.toggle(self.btn2),
        )
        self.btn3 = tk.Button(
            self.buttonframe,
            text="BTC",
            font=("Arial", 12),
            command=lambda: self.toggle(self.btn3),
        )

        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E, padx=20, pady=20)
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E, padx=20, pady=20)
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E, padx=20, pady=20)

        self.buttonframe.pack() # Buttons are related to toggle() function on line 72 to 94
        self.btn1.config(relief="sunken", bg="lightgray") # rendering USD button pressed since it's the default value

        self.confirm = tk.Button( # confirm button related to main() function on line 60 to 70
            self.root, text="Converter", font=("Arial", 18), command=self.main
        )
        self.confirm.pack(pady=10)

        self.root.resizable(False, False)
        self.root.mainloop() # Window init

    def main(self):
        print("=== Conversor de Moedas ===") # Console response to map where code is running
        try:
            self.entryValue = self.entry.get() # Get entry value
            tax = self.get_exchange_rate("BRL") # Get conversion value
            converted = round(float(self.entryValue) / float(tax), 3) # Here, the round function is necessary because when making this conversion by division, we get enormous values. Also it's necessary float values because most of them is a string type.
            self.conversion["text"] = f"{self.entryValue} BRL = {converted} {self.target}" # Giving response to client
            print(f"{self.entryValue} BRL = {converted} {self.target}")
        except Exception as e:
            self.conversion["text"] = "Erro ao obter cotação"
            print("Erro ao obter cotação:", e)

    def toggle(self, button):
        print(button.winfo_name())
        match button.winfo_name(): # It gets the name of the rendered object on the window. To avoid repetition and creation of new variables i just used values that already exit
            case "!button":
                self.target = button["text"]
                print(self.target)
                self.btn1.config(relief="sunken", bg="lightgray")
                self.btn2.config(relief="raised", bg="SystemButtonFace")
                self.btn3.config(relief="raised", bg="SystemButtonFace")
            case "!button2":
                self.target = button["text"]
                print(self.target)
                self.btn2.config(relief="sunken", bg="lightgray")
                self.btn1.config(relief="raised", bg="SystemButtonFace")
                self.btn3.config(relief="raised", bg="SystemButtonFace")
            case "!button3":
                self.target = button["text"]
                print(self.target)
                self.btn3.config(relief="sunken", bg="lightgray")
                self.btn2.config(relief="raised", bg="SystemButtonFace")
                self.btn1.config(relief="raised", bg="SystemButtonFace")
            case _:
                print("No button found")

    def get_exchange_rate(self, base="BRL"):
        url = f"https://economia.awesomeapi.com.br/json/last/{self.target}-{base}" # Usually, it'll be better switch the positios of "base" value and "target" value since it's better multiply than divide, however the BTC url is broken in that way.
        response = requests.get(url)
        print(response)
        data = response.json()
        print(data)
        return data[f"{self.target}{base}"]["high"] # get the hightest value of the coin on last hour. it searches for in on the dictionary get from url

Window() # class init
