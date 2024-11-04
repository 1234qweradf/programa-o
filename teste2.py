import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x600")
        
        self.resultado = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        entrada = tk.Entry(self.master, textvariable=self.resultado, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entrada.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+','%',
        ]

        linha = 1
        coluna = 0
        for botao in botoes:
            tk.Button(self.master, text=botao, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=botao: self.clique(b)).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        tk.Button(self.master, text='C', padx=20, pady=20, font=('Arial', 18), command=self.limpar).grid(row=linha, column=0)

    def clique(self, botao):
        if botao == '=':
            try:
                self.resultado.set(eval(self.resultado.get()))
            except Exception as e:
                self.resultado.set("Erro")
        else:
            self.resultado.set(self.resultado.get() + botao)

    def limpar(self):
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()