nome = input()
salario = float(input())
total_vendas = float(input())

salario_total = salario + total_vendas * 0.15

print(f'TOTAL = R$ {salario_total:.2f}')