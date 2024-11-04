def calcular_peso_ideal(altura, genero):
    if genero.lower() == "homem":
        return (72.7 * altura) - 58
    elif genero.lower() == "mulher":
        return (62.1 * altura) - 44.7
    else:
        return None
altura = float(input("Digite sua altura (em metros): "))
genero = input("Digite seu gênero (Homem ou Mulher): ")
peso_ideal = calcular_peso_ideal(altura, genero)
if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print ("Gênero inválido. Por favor, digite 'homem' ou 'mulher'.")