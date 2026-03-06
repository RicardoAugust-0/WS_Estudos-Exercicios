# Programa que pergunta ao usuário a velocidade de um carro, caso ultrapasse 80 km/h, deve exibir uma mensagem dizendo que o usuário foi multado. Nesse caso, deve exibir o valor da multa, cobrando R$5,00 reais por km acima do perimitido.

limite_velocidade = 80
velocidade_carro = int(input("Qual a velocidade do veículo? Coloque o valor em Km/h: "))

if velocidade_carro > limite_velocidade:
  multa = (velocidade_carro - 80) * 5
  print(f"Você foi multado em R${multa},00 reais!")
else:
  print("Você está dentro do limite de velocidade.")