valor = int(input())

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
#Cedulas de 1
cedulas1 = resto2 // 1

print(f"{valor}")
print(f"{cedulas100} nota(s) de R$ 100,00")
print(f"{cedulas50} nota(s) de R$ 50,00")
print(f"{cedulas20} nota(s) de R$ 20,00")
print(f"{cedulas10} nota(s) de R$ 10,00")
print(f"{cedulas5} nota(s) de R$ 5,00")
print(f"{cedulas2} nota(s) de R$ 2,00")
print(f"{cedulas1} nota(s) de R$ 1,00")

