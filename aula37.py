conto1=0
conto2=0
conto3=0
conto4=0
n=1
i = 1
while(i<3):
    n=int(input('dijite um valor: '))
    if(n>=0)and(n<=25):
        conto1+=1
    if(n>=26)and(n<=50):
        conto2+=1
    if(n>=51)and(n<=75):
        conto3+=1
    if(n>=76)and(n<=100):
        conto4+=1
    if(n < 0):
        i = 4
print('A quantidade de numeros no intervalo entre 0 a 25',conto1)
print('A quantidade de numerros no intervalo entre 26 a 50',conto2)
print('A quantidade de numerros no intervalo entre 51 a 75',conto3)
print('A quantidade de numerros no intervalo entre 76 a 100',conto4)
