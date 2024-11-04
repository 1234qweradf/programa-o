#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por
#meio de código.  Os códigos utilizados são:
#1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela 
#ex: 1 - Jose/ 2- João /3 - Maria/ 4 - Meu nego) 5 - Voto Nulo 6 - Voto em Branco
#Faça um programa que calcule e mostre:
#- O total de votos para cada candidato;
#- O total de votos nulos;
#- O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. 
#Para finalizar o algoritmo, o valor digitado deve ser igual a 0.
def main():
    # Inicializa as contagens
    votos = {
        1: 0,  # José
        2: 0,  # João
        3: 0,  # Maria
        4: 0,  # Meu Nego
        5: 0,  # Voto Nulo
        6: 0   # Voto em Branco
    }

    total_votos = 0

    print("Digite os votos (1: José, 2: João, 3: Maria, 4: Meu Nego, 5: Nulo, 6: Branco). Digite 0 para finalizar.")

    while True:
        voto =str(input("Digite o seu voto: "))
        
        if voto == 0:
            break
        
        if voto in votos:
            votos[voto] += 1
            total_votos += 1
        else:
            print("Voto inválido. Tente novamente.")

    if total_votos > 0:
        percent_nulos = (votos[5] / total_votos) * 100
        percent_brancos = (votos[6] / total_votos) * 100
    else:
        percent_nulos = 0
        percent_brancos = 0

    print("\nResultados da Eleição:")
    print(f"Total de votos para José: {votos[1]}")
    print(f"Total de votos para João: {votos[2]}")
    print(f"Total de votos para Maria: {votos[3]}")
    print(f"Total de votos para Meu Nego: {votos[4]}")
    print(f"Total de votos nulos: {votos[5]}")
    print(f"Total de votos em branco: {votos[6]}")
    print(f"Total de votos: {total_votos}")
    print(f"Percentagem de votos nulos: {percent_nulos:.2f}%")
    print(f"Percentagem de votos em branco: {percent_brancos:.2f}%")

if __name__ == "__main__":
    main()
