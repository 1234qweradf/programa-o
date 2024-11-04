# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
impar=0
par=0
for i in range(10):
    valor = int (input("informe o valor: "))
    if (valor %2==0):
        print("numerro é par")
        par=par+1
    else:
        print("o valor é inpar")
        inpar=inpar+1