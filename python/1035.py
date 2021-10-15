A, B, C, D = map(int, input().split(" "))
condicao = (B > C) & (D > A) & (C + D > A + B)

print(f'Valores aceitos') if condicao else print(f'Valores nao aceitos')