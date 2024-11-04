def calcular_bonus(valor):
    return valor * 0.10 if valor <= 50000 else valor * 0.15

clientes = []

for _ in range(15):
    nome = input("Nome do cliente: ")
    endereco = input("Endereço do cliente: ")
    valor_compras = float(input("Valor das compras: R$ "))
    
    bonus = calcular_bonus(valor_compras)
    
    clientes.append({"Nome": nome, "Endereço": endereco, "Valor das Compras": valor_compras, "Bônus": bonus})

print("\nCorrespondência enviada para os clientes:")
for cliente in clientes:
    print(f"\nCliente: {cliente['Nome']}")
    print(f"Endereço: {cliente['Endereço']}")
    print(f"Valor das Compras: R$ {cliente['Valor das Compras']:.2f}")
    print(f"Bônus: R$ {cliente['Bônus']:.2f}")
