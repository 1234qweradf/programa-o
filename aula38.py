 #Faça um algoritmo que receba a sigla da cidade de origem de um grupo de pessoas, ao final informe quantas foram 
#digitadas das cidades do Rio de Janeiro, Belo Horizonte e Santa Catarina (separadamente). O algoritmo encerra quando digitado a palavra “fim”.

contador_rj = 0
contador_bh = 0
contador_sc = 0

while True:
    
    sigla = input("Digite a sigla da cidade (ou 'fim' para encerrar): ")

    if sigla.lower() == "fim":
        break

    if sigla.upper() == "RJ":
        contador_rj += 1
    elif sigla.upper() == "BH":
        contador_bh += 1
    elif sigla.upper() == "SC":
        contador_sc += 

print("Total de cidades do Rio de Janeiro: ", contador_rj)
print("Total de cidades de Belo Horizonte: ", contador_bh)
print("Total de cidades de Santa Catarina: ", contador_sc)
