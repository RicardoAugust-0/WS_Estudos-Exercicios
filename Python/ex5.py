# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

print("Bem-vindo ao simulador de poupança!")
# Aqui eu declaro as variáveis que vou usar para calcular o valor do depósito inicial e a taxa de juros da poupança.
depInicial = int(input("Digite um valor de depósito inicial: "))
jurosPoupanca = int(input("Digite a taxa de juros da poupança: "))
mes = 1

# Aqui eu declaro a variável que vou usar para calcular o valor total do depósito.
valorTotal = depInicial

# Aqui eu uso um loop while para calcular o valor total do depósito mês a mês.
while mes <= 24:
  # Aqui eu calculo o valor total do depósito mês a mês.
  valorTotal = valorTotal + (valorTotal * jurosPoupanca / 100)
  # Aqui eu imprimo o valor total do depósito mês a mês.
  print(f"O valor do depósito no mês {mes} é de R${valorTotal:.2f}")
  # Aqui eu incremento o valor do mês.
  mes = mes + 1

# Aqui eu imprimo o valor total ganho com juros no período.
print(f"O valor total ganho com juros no período é de R${valorTotal - depInicial:.2f}")