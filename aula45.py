# Leitura e validação do nome
nome = input("Digite seu nome (maior que 3 caracteres): ")
if len(nome) <= 3:
    while len(nome) <= 3:
        print("Nome inválido. Deve ter mais que 3 caracteres.")
        nome = input("Digite seu nome (maior que 3 caracteres): ")

# Leitura e validação da idade
idade = int(input("Digite sua idade (0 a 150): "))
if idade < 0 or idade > 150:
    while idade < 0 or idade > 150:
        print("Idade inválida. Deve estar entre 0 e 150.")
        idade = int(input("Digite sua idade (0 a 150): "))

# Leitura e validação do salário
salario = float(input("Digite seu salário (maior que zero): "))
if salario <= 0:
    while salario <= 0:
        print("Salário inválido. Deve ser maior que zero.")
        salario = float(input("Digite seu salário (maior que zero): "))

# Leitura e validação do sexo
sexo = input("Digite seu sexo (f ou m): ").lower()
if sexo not in ['f', 'm']:
    while sexo not in ['f', 'm']:
        print("Sexo inválido. Deve ser 'f' ou 'm'.")
        sexo = input("Digite seu sexo (f ou m): ").lower()

# Leitura e validação do estado civil
estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()
if estado_civil not in ['s', 'c', 'v', 'd']:
    while estado_civil not in ['s', 'c', 'v', 'd']:
        print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
        estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()

# Exibição das informações
print("\nInformações Cadastradas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {estado_civil}")