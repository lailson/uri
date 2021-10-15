valor = float(input())

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
resto = valor

print(f'NOTAS:')
for n in notas:
  quantidade = resto // n
  resto = resto % n
  print(f'{quantidade} nota(s) de RS {n}')

print(f'MOEDAS:')
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
for m in moedas:
  quantidade = resto // m
  resto = resto % m
  print(f'{quantidade} moeda(s) de R$ {m}')