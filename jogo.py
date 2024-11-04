import tkinter as tk
from tkinter import messagebox

# Lista de perguntas e respostas
perguntas = [
    ("Qual a capital do Brasil?", "Brasília"),
    ("Qual o maior oceano do mundo?", "Oceano Pacífico"),
    ("Qual o planeta mais próximo do Sol?", "Mercúrio"),
    ("Quem escreveu 'Dom Quixote'?", "Miguel de Cervantes"),
    ("Qual é o metal mais abundante na Terra?", "Alumínio"),
    ("Qual é o país mais populoso do mundo?", "China"),
    ("Quem pintou a Mona Lisa?", "Leonardo da Vinci"),
    ("Qual é a maior montanha do mundo?", "Monte Everest"),
    ("Quem descobriu a América?", "Cristóvão Colombo"),
    ("Qual é o maior deserto do mundo?", "Deserto do Saara")
    

]

# Função para verificar a resposta
def verificar_resposta():
    resposta = resposta_entry.get()
    pergunta_atual = perguntas[pergunta_idx[0]]
    if resposta.lower() == pergunta_atual[1].lower():
        messagebox.showinfo("Correto!", "Você acertou!")
    else:
        messagebox.showinfo("Errado", f"A resposta correta é: {pergunta_atual[1]}")
    pergunta_idx[0] += 1
    if pergunta_idx[0] < len(perguntas):
        atualizar_pergunta()
    else:
        messagebox.showinfo("Fim do Jogo", "Você completou todas as perguntas!")

# Função para atualizar a pergunta
def atualizar_pergunta():
    pergunta_label.config(text=perguntas[pergunta_idx[0]][0])
    resposta_entry.delete(0, tk.END)

# Cria a janela principal
root = tk.Tk()
root.title("Jogo de Perguntas e Respostas")

# Inicializa o índice da pergunta
pergunta_idx = [0]

# Cria e posiciona os widgets
pergunta_label = tk.Label(root, text=perguntas[pergunta_idx[0]][0], font=("Arial", 14))
pergunta_label.pack(pady=20)

resposta_entry = tk.Entry(root, font=("Arial", 14))
resposta_entry.pack(pady=10)

verificar_button = tk.Button(root, text="Verificar", command=verificar_resposta, font=("Arial", 14))
verificar_button.pack(pady=20)

# Inicia o loop principal da aplicação
root.mainloop()

