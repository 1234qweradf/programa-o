total_vt = 0
total_vr = 0

for i in range(3):
    salario_base = float(input(f"Digite o salário-base do funcionário {i+1}: "))
    desconto_vt = salario_base * 0.02
    desconto_vr = salario_base * 0.03
    total_vt += desconto_vt
    total_vr += desconto_vr

print(f"Total de descontos com vale transporte: R$ {total_vt:.2f}")
print(f"Total de descontos com vale refeição: R$ {total_vr:.2f}")
