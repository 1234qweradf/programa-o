#1. Construa um
#algoritmo que receba cinquenta números e mostre a média dos números que foram digitados.
s=0
for i in range(1, 51):
    n= int(input("informe o valor: "))
    s = s + n
m=s/i
print(m)