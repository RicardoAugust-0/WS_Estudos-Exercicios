# Escrever um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números de somas sucessivas de um deles.

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

contador = n2
resultado = 0

while contador > 0:
  if n1 == 1:
    print(f"{n2}")
  else:
    resultado = resultado + n2
    contador -= 1

print(f"{resultado}")