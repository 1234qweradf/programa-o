#) Escreva um programa que gere a tabuada das multiplicações de um número inteiro n (1 n 10) recebido do teclado. A saída deverá ser semelhante ao exemplo abaixo:
n=int(input("informe um valor: "))
for i in range(1,11):
    resultado=n*i
    print(n,"x",i,"=",resultado)