codigo=int(input('digite o codigo de verificação: '))
num1=int(input('digite o total de vendas: '))
if (num1<100):
    print('a comisão aumentou 0%')
elif(num1 > 100) and num1 < 350:
    print('a comisão aumentou 6%')
    soma=(num1 / 6)+num1
    print(soma)
elif num1 > 350:
    print ('a comisão aumentou10%')
    soma=(num1/10)+num1
    print(soma)