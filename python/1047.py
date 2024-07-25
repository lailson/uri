def calcular_duracao_jogo():
    hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

    inicio_em_minutos = hora_inicial * 60 + minuto_inicial
    fim_em_minutos = hora_final * 60 + minuto_final

    # Caso o tempo de término seja menor que o tempo de início, ajusta para o dia seguinte
    if fim_em_minutos <= inicio_em_minutos: 
        fim_em_minutos += 24 * 60

    # Calcula a duração total em minutos
    duracao_em_minutos = fim_em_minutos - inicio_em_minutos

    # Converte a duração em horas e minutos
    duracao_horas = duracao_em_minutos // 60
    duracao_minutos = duracao_em_minutos % 60

    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")


calcular_duracao_jogo()
