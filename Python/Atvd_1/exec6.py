# Programa para calcular o tempo médio de uma viagem de carro.

# Solicita ao usuário a distância a ser percorrida e a velocidade média.

distancia = float(input("Digite a distância a ser percorrida em km: "))
velocidade = float(input("Digite a velocidade média em km/h: "))

# Calcula o tempo médio de viagem.
tempo = distancia / velocidade

# Exibe o resultado.
print(f"O tempo médio de viagem é de {tempo} horas.")
print(f"O tempo médio de viagem é de {tempo * 60} minutos.")