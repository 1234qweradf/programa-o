# Lê 50 números e conta os negativos
negativos = sum(1 for i in range(5)
if float(input(f"Digite o {i+1}º número: ")) < 0)

print(f"Total de números negativos: {negativos}")
