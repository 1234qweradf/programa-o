import random

def jogar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogo_craps():
    primeiro_lancamento = jogar_dados()
    print(f"Você tirou {primeiro_lancamento}")

    if primeiro_lancamento in [7, 11]:
        print("Parabéns, você tirou um natural e ganhou!")
    elif primeiro_lancamento in [2, 3, 12]:
        print("Craps! Você perdeu.")
    else:
        ponto = primeiro_lancamento
        print(f"Seu ponto é {ponto}. Continue jogando até tirar {ponto} novamente. Se tirar 7 antes, você perde.")
        while True:
            novo_lancamento = jogar_dados()
            print(f"Você tirou {novo_lancamento}")
            if novo_lancamento == ponto:
                print("Parabéns, você tirou seu ponto novamente e ganhou!")
                break
            elif novo_lancamento == 7:
                print("Você tirou um 7 e perdeu.")
                break

def main():
    while True:
        jogo_craps()
        repetir = input("Deseja jogar novamente? (s/n): ").lower()
        if repetir != 's':
            break

# Inicia o jogo
main()
