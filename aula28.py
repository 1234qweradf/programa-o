#Escrever um algoritmo que leia 50 números e informe quantos
#destes valores são negativos.
# Inicializa um contador para os números negativos
contador_negativos = 0
# Loop para ler 50 números
for i in range(50):
    numero = float(input(f"Digite o {i+1}º número: "))  # Lê o número do usuário
    if numero < 0:  # Verifica se o número é negativo
        contador_negativos += 1  # Incrementa o contador se for negativo
# Exibe o total de números negativos
print(f"Total de números negativos: {contador_negativos}")