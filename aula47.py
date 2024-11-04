nome = input("Nome (mais que 3 caracteres): ")
while len(nome) <= 3:
    nome = input("Inválido. Digite novamente: ")

idade = int(input("Idade (0 a 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Inválido. Digite novamente: "))

salario = float(input("Salário (maior que zero): "))
while salario <= 0:
    salario = float(input("Inválido. Digite novamente: "))

sexo = input("Sexo (f ou m): ")
while True:
    if sexo == 'f' or sexo == 'm':
        break
    sexo = input("Inválido. Digite novamente (f ou m): ")

estado_civil = input("Estado civil (s, c, v, d): ")
while True:
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    estado_civil = input("Inválido. Digite novamente (s, c, v, d): ")

print(f"\nNome: {nome}\nIdade: {idade}\nSalário: R${salario:.2f}\nSexo: {'Feminino' if sexo == 'f' else 'Masculino'}\nEstado Civil: {estado_civil}")
