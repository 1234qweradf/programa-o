#4
def gerar_fibonacci(limite):
    fibonacci = [0, 1]
    while True:
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo > limite:
            break
        fibonacci.append(proximo)
    return fibonacci

serie = gerar_fibonacci(500)
print(serie)
