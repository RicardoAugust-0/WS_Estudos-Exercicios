# Programa que leia um valor e imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. Para simplificar vamos trabalar apenas com valores inteiros e com cédulas de R$ 50, R$ 20, R$ 10, R$ 5 e R$1.

valor = int(input("Coloque um valor para ser aplicada a quantidade de cédulas necessárias: "))

cedulas50 = 50
cedulas20 = 20
cedulas10 = 10
cedulas5 = 5
cedula1 = 1
valor_total = 0

while valor > 0:
  if valor >= cedulas50:
      valor_total = valor // cedulas50
      print(f"Quantidade de cédulas de R$ 50: {valor_total}")
      valor = valor - (valor_total * cedulas50)
      valor_total = 0

  elif valor >= cedulas20:
      valor_total = valor // cedulas20
      print(f"Quantidade de cédulas de R$ 20: {valor_total}")
      valor = valor - (valor_total * cedulas20)
      valor_total = 0

  elif valor >= cedulas10:
      valor_total = valor // cedulas10
      print(f"Quantidade de cédulas de R$ 10: {valor_total}")
      valor = valor - (valor_total * cedulas10)
      valor_total = 0

  elif valor >= cedulas5:
      valor_total = valor // cedulas5
      print(f"Quantidade de cédulas de R$ 5: {valor_total}")
      valor = valor - (valor_total * cedulas5)
      valor_total = 0

  elif valor >= cedula1:
      valor_total = valor // cedula1
      print(f"Quantidade de cédulas de R$ 1: {valor_total}")
      valor = valor - (valor_total * cedula1)
      valor_total = 0
  else:
      print("Valor inválido")
      break