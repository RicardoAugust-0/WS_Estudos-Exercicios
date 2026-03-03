dias = input("Digite a quantidade de dias: ")
horas = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
segundos = input("Digite a quantidade de segundos: ")

total_segundos = dias * 86000 + horas * 3600 + minutos * 60 + segundos

print(f"O total de segundos é {total_segundos}")