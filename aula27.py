#ue receba 100 números, e conte quantos deles estão no intervalo [10, 20] e quantos deles estão fora do intervalo, escrevendo estas informações.
# Inicializa as contagens
dentro_intervalo = 0
fora_intervalo = 0

# Recebe 100 números do usuário
for i in range(100):
    numero = float(input(f"Digite o {i+1}º número: "))
    if 10 <= numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

# Exibe os resultados
print(f"Números dentro do intervalo [10, 20]: {dentro_intervalo}")
print(f"Números fora do intervalo [10, 20]: {fora_intervalo}")