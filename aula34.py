# Inicializa contadores
contagem_P = 0
contagem_M = 0
contagem_G = 0
contagem_GG = 0

# Laço para receber os tamanhos das camisetas
for i in range(50):
    tamanho = input(f"Digite o tamanho da camiseta {i+1} (P, M, G, GG): ").strip().upper()
    
    if tamanho == 'P':
        contagem_P += 1
    elif tamanho == 'M':
        contagem_M += 1
    elif tamanho == 'G':
        contagem_G += 1
    elif tamanho == 'GG':
        contagem_GG += 1
    else:
        print("Tamanho inválido! Digite apenas P, M, G ou GG.")

# Exibe o total de camisetas por tamanho
print(f"Total de camisetas P: {contagem_P}")
print(f"Total de camisetas M: {contagem_M}")
print(f"Total de camisetas G: {contagem_G}")
print(f"Total de camisetas GG: {contagem_GG}")
