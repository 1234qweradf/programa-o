#Construa um algoritmo que receba 30 números e mostre a soma total dos números recebidos.
soma=0
for i in range(30):
    valor=int(input("informe um numero"))
    soma = soma+valor
    print(soma)