tempo = int(input())

horas = tempo // (60*60)
minutos = (tempo // 60) - (60 * horas)
segundos = (tempo % 60) 
print(f'{horas}:{minutos}:{segundos}')