# Soma dos números ímpares em um intervalo. Elabore um programa em Python que leia dois números inteiros, representando um intervalo, e calcule a soma de todos os números ímpares existentes entre eles, incluindo os extremos, se forem ímpares. Exemplo: se o usuário digitar 3 e 9 o programa deverá somar: 3 + 5 + 7 + 9 = 24. O programa deve ler dois valores; percorrer o intervalo com while; identificar os números ímpares e exibir a soma final.

# Leitura dos dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Inicio da lógica
soma = 0

# Condição 
if numero1 > numero2:
  numero1, numero2 = numero2, numero1

# Loop para percorrer o intervalo
while numero1 <= numero2:
  if numero1 % 2 != 0:
    soma = soma + numero1
    numero1 = numero1 + 1

  elif numero1 % 2 == 0:
    numero1 = numero1 + 1

  else:
    print("Número inválido")

# Resultado
print(soma)