import tkinter as tk

def __init__():
  root = tk.Tk()
  root.title("Conversor de moedas")

  btn = [tk.Button(root,text="PRS",font=("Arial", 12)),tk.Button(root,text="PRS",font=("Arial", 12)),tk.Button(root,text="NPS",font=("Arial", 12)),tk.Button(root,text="PRS",font=("Arial", 12))]
  for a in range(len(btn)):
    btn[a].pack()

  btn[2].config(relief="sunken", bg="lightgray")

  root.mainloop()

__init__()