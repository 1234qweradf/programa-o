def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

def main():
    print("Calculadora Simples")
    print("Operações disponíveis: soma, subtracao, multiplicacao, divisao")
    
    while True:
        operacao = input("Digite a operação (ou 'sair' para encerrar): ")
        if operacao.lower() == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = calcular(operacao, num1, num2)
            print(f"O resultado é: {resultado}")
        except ValueError:
            print("Por favor, insira números válidos.")

if __name__ == "__main__":
    main()