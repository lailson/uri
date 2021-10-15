valor = float(input())

## Essa parte é do problema 1018
# Cedulas de 100
cedulas100 = valor // 100
resto100 = valor % 100
# Cedulas de 50
cedulas50 = resto100 // 50
resto50 = resto100 % 50
# Cedulas de 20
cedulas20 = resto50 // 20
resto20 = resto50 % 20
# Cedulas de 10
cedulas10 = resto20 // 10
resto10 = resto20 % 10
# Cedulas de 5
cedulas5 = resto10 // 5
resto5 = resto10 % 5
# Cedulas de 2
cedulas2 = resto5 // 2
resto2 = resto5 % 2

#moedas de 1
moedas1 = resto2 // 1
#moedas de 0.50
centavos = valor % 1
moedas50 = centavos // 0.50
resto50c = centavos % 0.50
#moedas de 25
moedas25 = resto50c // 0.25
resto25c = resto50c % 0.25
#moedas de 10
moedas10 = resto25c // 0.10
resto10c = resto25c % 0.10
#moedas de 5
moedas05 = resto10c// 0.05
resto05c = resto10c % 0.05
#moedasde 1
moedas01 = resto05c // 0.01


print(f"NOTAS:")
print(f"{cedulas100} nota(s) de R$ 100.00")
print(f"{cedulas50} nota(s) de R$ 50.00")
print(f"{cedulas20} nota(s) de R$ 20.00")
print(f"{cedulas10} nota(s) de R$ 10.00")
print(f"{cedulas5} nota(s) de R$ 5.00")
print(f"{cedulas2} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{moedas1} moeda(s) de R$ 1.00")
print(f"{moedas50} moeda(s) de R$ 0.50")
print(f"{moedas25} moeda(s) de R$ 0.25")
print(f"{moedas10} moeda(s) de R$ 0.10")
print(f"{moedas05} moeda(s) de R$ 0.05")
print(f"{moedas01} moeda(s) de R$ 0.01")
