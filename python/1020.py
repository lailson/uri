tempo = int(input())

anos = tempo // 365
meses = (tempo % 365) // 30
dias = ( tempo % 365 ) - (30 * meses) 
print(f'{anos} ano(s)')
print(f'{meses} meses(es)')
print(f'{dias} dias(s)')