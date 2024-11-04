#7) 
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

def verificar_respostas(aluno_respostas):
    acertos = 0
    for i in range(10):
        if aluno_respostas[i].upper() == gabarito[i]:
            acertos += 1
    return acertos

def main():
    alunos = []
    while True:
        respostas = []
        for i in range(10):
            resposta = input(f'Qual sua resposta para a questão {i+1}? ')
            respostas.append(resposta)
        
        acertos = verificar_respostas(respostas)
        alunos.append(acertos)
        
        outro_aluno = input('Outro aluno vai utilizar o sistema? (s/n): ')
        if outro_aluno.lower() != 's':
            break
    
    if alunos:
        maior_acerto = max(alunos)
        menor_acerto = min(alunos)
        total_alunos = len(alunos)
        media_notas = sum(alunos) / total_alunos

        print(f'\nMaior acerto: {maior_acerto}')
        print(f'Menor acerto: {menor_acerto}')
        print(f'Total de alunos: {total_alunos}')
        print(f'Média das notas da turma: {media_notas:.2f}')
    else:
        print('Nenhum aluno utilizou o sistema.')

if __name__ == "__main__":
    main()
