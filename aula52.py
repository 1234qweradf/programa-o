#6
def encontrar_alturas():
    alunos = []
    for i in range(10):
        numero_aluno = int(input(f'Informe o número do aluno {i+1}: '))
        altura_aluno = float(input(f'Informe a altura do aluno {numero_aluno} em cm: '))
        alunos.append((numero_aluno, altura_aluno))
    
    aluno_mais_alto = max(alunos, key=lambda x: x[1])
    aluno_mais_baixo = min(alunos, key=lambda x: x[1])

    print(f'O aluno mais alto é o número {aluno_mais_alto[0]} com {aluno_mais_alto[1]} cm.')
    print(f'O aluno mais baixo é o número {aluno_mais_baixo[0]} com {aluno_mais_baixo[1]} cm.')

if __name__ == "__main__":
    encontrar_alturas()
