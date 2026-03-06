# Programa que pergunta o salário de um funcionário e calcula o valor de aumento. Para salários superiores a R$1.250,00 é necessário calcular um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = int(input("Adicione o valor de seu salário: "))

if (salario > 1250):
  aumento = 0.10
  salario_final = salario * aumento
  print(f"Seu salário com aumento é de aproximadamente {salario_final}")
elif (salario <= 1250):
  aumento = 0.15
  salario_final = salario * aumento
  print(f"Seu salário com aumento é de aproximadamente {salario_final}")
else:
  print("")