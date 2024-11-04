# Inicializa variáveis para armazenar os valores
#que receba o peso, a idade e a altura de cem pessoas, calcule e informe os valores de: maior peso, menor peso, maior
#a#ltura, menor altura, maior idade e menor idade deste grupo de pessoas.vv
maior_peso = float('-inf')
menor_peso = float('inf')
maior_altura = float('-inf')
menor_altura = float('inf')
maior_idade = float('-inf')
menor_idade = float('inf')
# Loop para ler os dados de 100 pessoas
for i in range(10):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    # Atualiza o maior e menor peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
    # Atualiza o maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    # Atualiza o maior e menor idade
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
# Exibe os resultados
print(f"Maior peso: {maior_peso} kg")
print(f"Menor peso: {menor_peso} kg")
print(f"Maior altura: {maior_altura} m")
print(f"Menor altura: {menor_altura} m")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")