entrada = input().split()
dia_inicio = int(entrada[1])
entrada = input().split(':')
hora_inicio = int(entrada[0])
minuto_inicio = int(entrada[1])
segundo_inicio = int(entrada[2])
entrada = input().split()
dia_fim = int(entrada[1])
entrada = input().split(':')
hora_fim = int(entrada[0])
minuto_fim = int(entrada[1])
segundo_fim = int(entrada[2])
duracao_segundos = (dia_fim - dia_inicio) * 86400 + (hora_fim - hora_inicio) * 3600 + (minuto_fim - minuto_inicio) * 60 + (segundo_fim - segundo_inicio)
duracao_dias = duracao_segundos // 86400
duracao_segundos = duracao_segundos % 86400
duracao_horas = duracao_segundos // 3600
duracao_segundos = duracao_segundos % 3600
duracao_minutos = duracao_segundos // 60
duracao_segundos = duracao_segundos % 60
print("{} dia(s)".format(duracao_dias))
print("{} hora(s)".format(duracao_horas))
print("{} minuto(s)".format(duracao_minutos))
print("{} segundo(s)".format(duracao_segundos))