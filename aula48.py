#Faça um programa 
#que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
n=int(input("digite um numerro: "))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("não é um numerr primo")
            break
        else:
            print("é um numero primo")
            break
else:
    print('não é u numerro primo')